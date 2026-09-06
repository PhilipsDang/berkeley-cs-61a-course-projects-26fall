from pytest_grader import points


@points(1)
def take_turn():
    """
    >>> from hog import *
    >>> take_turn(2, 7, 27, make_test_dice(4, 5, 1))
    LOCKED: 8ccd6c1f2857e384

    >>> take_turn(3, 15, 9, make_test_dice(4, 6, 1))
    LOCKED: 75d4914b5829973f

    >>> take_turn(0, 12, 41) # what happens when you roll 0 dice?
    LOCKED: 9ee0a431797312e7

    """


@points(1)
def take_turn_examples():
    """
    >>> from hog import *
    >>> take_turn(0, 37, 15)
    18

    >>> take_turn(0, 35, 21)
    9

    >>> take_turn(2, 15, 25, make_test_dice(6))
    12

    >>> take_turn(9, 2, 3, make_test_dice(4))
    36

    >>> take_turn(7, 4, 11, make_test_dice(4))
    28

    >>> take_turn(8, 3, 15, make_test_dice(5))
    40

    >>> take_turn(1, 3, 6, make_test_dice(5, 1))
    5

    >>> take_turn(2, 3, 4, make_test_dice(5, 1))
    1


    >>> import hog
    >>> def roll_dice(num_rolls, dice):
    ...     print("Called roll dice!")
    ...     return 9002
    ...
    >>> hog.roll_dice, old_roll_dice = roll_dice, hog.roll_dice
    >>> hog.take_turn(5, 0, 0) # Make sure you call roll_dice!
    Called roll dice!
    9002

    >>> def boar_brawl(player_score, opponent_score):
    ...     print("Called boar brawl!")
    ...     return 9001
    ...
    >>> hog.boar_brawl, old_boar_brawl = boar_brawl, hog.boar_brawl
    >>> hog.take_turn(0, 12, 41) # Make sure you call boar_brawl when rolling 0 dice!
    Called boar brawl!
    9001
    >>> hog.take_turn(3, 12, 41, make_test_dice(2)) # ... and roll_dice otherwise
    Called roll dice!
    9002

    """
