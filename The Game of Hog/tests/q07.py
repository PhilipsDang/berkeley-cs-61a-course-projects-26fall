from pytest_grader import points


@points(1)
def is_always_roll():
    """
    >>> from hog import *
    >>> is_always_roll(always_roll_5)
    LOCKED: 46851156286089fd

    >>> is_always_roll(always_roll(3))
    LOCKED: 2813f1a90ea88d27

    >>> is_always_roll(catch_up)
    LOCKED: fb410b80763dded2

    """


@points(1)
def is_always_roll_examples():
    """
    >>> from hog import *
    >>> def s(x, y):
    ...    if x == 0 and y == 0:
    ...        return 0
    ...    else:
    ...        return 1
    >>> is_always_roll(s)
    False

    >>> def s(x, y):
    ...    if x == 60 and y == 0:
    ...        return 0
    ...    else:
    ...        return 1
    >>> is_always_roll(s)
    False

    >>> def s(x, y):
    ...    if x == 0 and y == 60:
    ...        return 0
    ...    else:
    ...        return 1
    >>> is_always_roll(s)
    False

    >>> def s(x, y):
    ...    if x == 60 and y == 60:
    ...        return 0
    ...    else:
    ...        return 1
    >>> is_always_roll(s)
    False

    >>> def s(x, y):
    ...    if x == 99 and y == 99:
    ...        return 0
    ...    else:
    ...        return 1
    >>> is_always_roll(s)
    False

    >>> def s(x, y):
    ...    if x == 150 and y == 125:
    ...        return 0
    ...    else:
    ...        return 1
    >>> is_always_roll(s, 200) # GOAL is not always 100!
    False

    """
