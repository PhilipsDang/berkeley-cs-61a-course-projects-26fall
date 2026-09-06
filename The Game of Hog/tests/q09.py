from pytest_grader import points


@points(1)
def max_scoring_num_rolls():
    """
    >>> from hog import *
    >>> dice = make_test_dice(3)   # dice always returns 3
    >>> max_scoring_num_rolls(dice, iterations=1000)
    LOCKED: 22578ee234be2e03

    >>> dice = make_test_dice(2)     # dice always rolls 2
    >>> max_scoring_num_rolls(dice, iterations=1000)
    LOCKED: 0b5d6c8aeffb69b8

    >>> dice = make_test_dice(1)     # dice always rolls 1
    >>> max_scoring_num_rolls(dice, iterations=1000)
    LOCKED: 7f7f538646741d0d

    >>> dice = make_test_dice(1, 2)  # dice alternates 1 and 2
    >>> max_scoring_num_rolls(dice, iterations=1000)
    LOCKED: 10b68b4c18b68f2d

    """


@points(1)
def max_scoring_num_rolls_examples():
    """
    >>> from hog import *
    >>> dice = make_test_dice(1, 2, 2, 2, 2, 2, 2, 2)
    >>> max_scoring_num_rolls(dice, iterations=1000)
    4

    >>> dice = make_test_dice(*([2] * 55 + [1, 2] * 500)) # test that you are not rolling the dice more than necessary
    >>> max_scoring_num_rolls(dice, iterations=1) # dice is 2 for the first 55 rolls, then is 1 followed by 2 for 1000 rolls
    10

    >>> # 100 2s and then 100 1s (don't worry about how this works)
    >>> dice = make_test_dice(*([2] * 100 + [1] * 100))
    >>> max_scoring_num_rolls(dice, iterations=1)
    10

    >>> dice = make_test_dice(1, 2, 3, 4, 5)  # dice sweeps from 1 through 5
    >>> max_scoring_num_rolls(dice, iterations=1000)
    3

    >>> dice = make_test_dice(6, 5, 4, 3, 2, 1)  # dice sweeps from 1 through 6
    >>> max_scoring_num_rolls(dice, iterations=1) # ensure iterations is being used
    4

    >>> import hog
    >>> averaged_functions = []
    >>> def make_averaged(func_to_average, iterations=1000):
    ...     averaged_functions.append(func_to_average)
    ...     def averaged(*args):
    ...         return 100 if args[0] == 7 else 0  # 7 rolls is best according to this fake average
    ...     return averaged
    ...
    >>> hog.make_averaged, old_make_averaged = make_averaged, hog.make_averaged
    >>> max_scoring_num_rolls(make_test_dice(6), iterations=1) # Make sure you call make_averaged and use the function it returns!
    7
    >>> len(averaged_functions) > 0
    True

    """
