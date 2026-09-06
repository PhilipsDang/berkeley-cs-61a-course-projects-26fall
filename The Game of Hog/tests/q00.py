from pytest_grader import points


@points(0)
def test_dice():
    """
    >>> from hog import *
    >>> test_dice = make_test_dice(4, 1, 2)
    >>> test_dice()
    LOCKED: d23d9396af481d2b
    >>> test_dice() # Second call
    LOCKED: 12f8327524a6dbb6
    >>> test_dice() # Third call
    LOCKED: b65d3eaa98baa95a
    >>> test_dice() # Fourth call
    LOCKED: c2672a4eec328c18
    >>> test_dice() # Fifth call
    LOCKED: 352bcb7a8b9dcbf8

    """
