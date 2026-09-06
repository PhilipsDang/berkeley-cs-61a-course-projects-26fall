from pytest_grader import points


@points(1)
def boar_strategy():
    """
    >>> from hog import *
    >>> boar_strategy(40, 51, threshold=7, num_rolls=2)
    LOCKED: b5e7abf47fdf4505

    >>> boar_strategy(40, 51, threshold=15, num_rolls=7)
    LOCKED: 9b8ea5739cda7fe6

    >>> boar_strategy(40, 51, threshold=16, num_rolls=7)
    LOCKED: de16a167199c0d88

    """


@points(1)
def boar_strategy_examples():
    """
    >>> from hog import *
    >>> boar_strategy(44, 53, threshold=3, num_rolls=2)
    0

    >>> boar_strategy(44, 53, threshold=4, num_rolls=2)
    2

    >>> boar_strategy(40, 31, threshold=9, num_rolls=5)
    0

    >>> boar_strategy(40, 31, threshold=10, num_rolls=5)
    5

    >>> boar_strategy(40, 52, threshold=15, num_rolls=2)
    0

    >>> boar_strategy(40, 52, threshold=16, num_rolls=2)
    2

    >>> s = 0
    >>> while s < 100:
    ...     if boar_brawl(90, s) >= 10:
    ...         assert boar_strategy(90, s, threshold=10, num_rolls=3) == 0
    ...     else:
    ...         assert boar_strategy(90, s, threshold=10, num_rolls=3) == 3
    ...     s += 1

    """
