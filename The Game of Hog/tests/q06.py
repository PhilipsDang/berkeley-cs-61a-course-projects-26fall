from pytest_grader import points


@points(2)
def always_roll():
    """
    >>> from hog import *
    >>> always_roll(3)(10, 20)
    LOCKED: 90e227a73bc1f4d0

    >>> always_roll(0)(99, 99)
    LOCKED: 53c372ef00f7343d

    """
