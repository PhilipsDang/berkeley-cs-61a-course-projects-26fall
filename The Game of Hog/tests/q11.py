from pytest_grader import points


@points(1)
def sus_strategy():
    """
    >>> from hog import *
    >>> sus_strategy(31, 21, threshold=10, num_rolls=2)
    LOCKED: 17fdaf07d5aae5d4

    >>> sus_strategy(30, 41, threshold=10, num_rolls=2)
    LOCKED: 17e35f726872ca0d

    >>> sus_strategy(53, 60, threshold=14, num_rolls=2)
    LOCKED: 574daefb17904e73

    >>> sus_strategy(53, 60, threshold=15, num_rolls=2)
    LOCKED: 7c5a8a9c2446af94

    >>> sus_strategy(23, 54, threshold=4, num_rolls=2)
    LOCKED: 8ba1930593e48318

    >>> sus_strategy(14, 21, threshold=8, num_rolls=2)
    LOCKED: a8404a8ebfc1214c

    >>> sus_strategy(14, 21, threshold=12, num_rolls=5)
    LOCKED: dd45c639158e9d6c

    """


@points(1)
def sus_strategy_examples():
    """
    >>> from hog import *
    >>> s = 0
    >>> while s < 100:
    ...     if sus_update(0, 20, s) - 20 >= 10:
    ...         assert sus_strategy(20, s, threshold=10, num_rolls=3) == 0
    ...     else:
    ...         assert sus_strategy(20, s, threshold=10, num_rolls=3) == 3
    ...     s += 1

    """
