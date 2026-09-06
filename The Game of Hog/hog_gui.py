"""Server for the Hog GUI.

Calls hog.play() once per game in a background thread. Strategy functions
block on a queue, waiting for the client to POST /roll with each move.
This is similar to hog_ui.py's interactive_strategy blocking on input().

Run from the hog/ directory: python3 hog_gui.py
"""

import importlib
import inspect
import json
import os
import queue
import secrets
import threading
import time
import webbrowser
from http import HTTPStatus
from http.server import HTTPServer, SimpleHTTPRequestHandler
from ucb import main
from urllib.parse import urlparse, parse_qs

import hog
import dice

PORT = 31415
STATIC_DIR = "gui-files/"
GAME_TIMEOUT = 60 * 60 * 24  # One day in seconds


class Game:
    def __init__(self, strategy_name=None):
        self.move_q = queue.Queue()
        self.result_q = queue.Queue()
        self.vs_computer = strategy_name is not None
        self.last_access = time.time()


games = {}


def get_strategies():
    """Return names of all strategy functions defined in hog.py.

    A strategy function takes (score, opponent_score, ...) and returns a
    number of dice to roll."""
    result = []
    for name, obj in inspect.getmembers(hog, inspect.isfunction):
        if name.startswith('_'):
            continue
        params = list(inspect.signature(obj).parameters.keys())
        if len(params) >= 2 and params[0] == 'score' and params[1] == 'opponent_score':
            result.append(name)
    return result


STRATEGIES = get_strategies()

def order_scores(who, score, opponent_score):
    """Return [Player 0 score, Player 1 score]."""
    if who == 0:
        return [score, opponent_score]
    else:
        return [opponent_score, score]

def start_game(game, strategy_name=None):
    """Start a game of Hog in a background thread.

    Each strategy function, when called by hog.play, reports the *previous*
    turn's results (dice outcomes and updated scores) before waiting for or
    computing its own move. The game-over result is sent after hog.play returns.
    """
    game_dice = dice.make_fair_dice(6)
    turn_outcomes = []

    def recording_dice():
        turn_outcomes.append(game_dice())
        return turn_outcomes[-1]

    last_player: list = [None]  # A one-element list to allow mutation

    def web_strategy(score, opponent_score):
        return game.move_q.get()

    def make_reporting_strategy(who, strategy):
        def reporting_strategy(score, opponent_score):
            scores = order_scores(who, score, opponent_score)
            game.result_q.put({"rolls": list(turn_outcomes), "scores": scores,
                               "who": who, "player": last_player[0],
                               "gameOver": False})
            turn_outcomes.clear()
            last_player[0] = who
            return strategy(score, opponent_score)
        return reporting_strategy

    strat0, strat1 = web_strategy, web_strategy
    if strategy_name:
        strat1 = getattr(hog, strategy_name)  # use a hog.py strategy function instead

    def run():
        s0, s1 = hog.play(make_reporting_strategy(0, strat0),
                          make_reporting_strategy(1, strat1),
                          hog.sus_update, 0, 0, dice=recording_dice, goal=100)
        game.result_q.put({"rolls": list(turn_outcomes), "scores": [s0, s1],
                           "who": 0 if s0 > s1 else 1,
                           "gameOver": True})

    threading.Thread(target=run, daemon=True).start()


def cleanup_stale_games():
    now = time.time()
    stale = [gid for gid, g in games.items() if now - g.last_access > GAME_TIMEOUT]
    for gid in stale:
        del games[gid]


def new_game(strategy_name=None):
    cleanup_stale_games()
    game_id = secrets.token_urlsafe(12)
    game = Game(strategy_name)
    games[game_id] = game
    start_game(game, strategy_name)
    game.result_q.get()  # synchronize: discard initial turn prompt
    return {"gameId": game_id}


def roll(game, num_dice):
    game.last_access = time.time()
    game.move_q.put(num_dice)
    result = game.result_q.get()
    results = [result]
    if game.vs_computer and not result["gameOver"]:
        computer_result = game.result_q.get()
        results.append(computer_result)
    return results


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=STATIC_DIR, **kwargs)

    def do_GET(self):
        if self.path == "/strategies":
            self.send_json(STRATEGIES)
        elif self.path.startswith("/dice_graphic.svg"):
            num = int(parse_qs(urlparse(self.path).query).get("num", ["1"])[0])
            svg = graphics.dice[num]
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "image/svg+xml")
            self.end_headers()
            self.wfile.write(svg.encode())
        else:
            super().do_GET()

    def do_POST(self):
        try:
            length = int(self.headers["Content-Length"])
            data = json.loads(self.rfile.read(length).decode())
            if self.path == "/roll":
                game = games.get(data.get("gameId"))
                if not game:
                    self.send_error(HTTPStatus.NOT_FOUND, "Game not found")
                    return
                result = roll(game, data["numDice"])
            elif self.path == "/new_game":
                result = new_game(data.get("strategy") or None)
            else:
                self.send_error(HTTPStatus.NOT_FOUND)
                return
            self.send_json(result)
        except Exception as e:
            print(e)
            self.send_error(HTTPStatus.INTERNAL_SERVER_ERROR)

    def send_json(self, data):
        body = json.dumps(data).encode()
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


@main
def run(*args):
    """Start the Hog GUI server."""
    import argparse

    parser = argparse.ArgumentParser(description="Hog GUI server")
    parser.add_argument(
        "--graphics", "-g", default="default_graphics",
        help="Module providing dice graphics (default: default_graphics)",
    )
    args = parser.parse_args()

    global graphics
    graphics = importlib.import_module(args.graphics)

    # Deployed (as on Cloud Run), $PORT says which port to serve on; locally,
    # try a few ports in case one is busy and open a browser once one works.
    hosted = "PORT" in os.environ
    first = int(os.environ.get("PORT", PORT))
    host = "0.0.0.0" if hosted else "localhost"
    server, port = None, first
    while server is None and port < first + (1 if hosted else 10):
        try:
            server = HTTPServer((host, port), Handler)
        except OSError:
            port += 1
    if server is None:
        print(f"Could not find an open port in range {first}-{port - 1}.")
        raise SystemExit(1)
    url = f"http://localhost:{port}"
    print(f"Hog GUI server running at {url}")
    if not hosted:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        server.socket.close()
