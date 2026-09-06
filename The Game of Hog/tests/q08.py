from pytest_grader import points


@points(1)
def make_averaged():
    """
    >>> from hog import *
    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> # Average of calling dice 1000 times
    >>> averaged_dice()
    LOCKED: 411e11d72d7ff48d

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_roll_dice = make_averaged(roll_dice, 1000)
    >>> # Average of calling roll_dice 1000 times
    >>> averaged_roll_dice(2, dice)
    LOCKED: 6204b3fc13219750

    """


@points(1)
def make_averaged_examples():
    """
    >>> from hog import *
    >>> hundred_range = range(1, 100)
    >>> hundred_dice = make_test_dice(*hundred_range)
    >>> averaged_hundred_dice = make_averaged(hundred_dice, 5*len(hundred_range))
    >>> correct_average = sum(range(1, 100)) / len(hundred_range)
    >>> averaged_hundred_dice()
    50.0
    >>> averaged_hundred_dice()
    50.0

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_roll_dice = make_averaged(roll_dice, 1)
    >>> averaged_roll_dice(2, dice)
    1.0

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_roll_dice = make_averaged(roll_dice, 5)
    >>> averaged_roll_dice(2, dice)
    5.0

    """
