from pytest_grader import points


@points(1)
def sus_fuss():
    """
    >>> from hog import *

    >>> num_factors(1)
    LOCKED: 2b358954832e7118

    >>> num_factors(2)
    LOCKED: 714e2ccf4065a8ac

    >>> num_factors(3)
    LOCKED: 476c32b15fca0455

    >>> num_factors(8)
    LOCKED: 4cae6145071e509a

    >>> num_factors(9)
    LOCKED: 413a2ae676c59722

    >>> sus_points(2)  # 2 is not sus
    LOCKED: 5b97613d725854f6

    >>> sus_points(8)  # 8 is sus
    LOCKED: 35d2d64eb801d890

    >>> num_rolls = 1
    >>> simple_update(num_rolls, 1, 3, make_test_dice(5))
    LOCKED: 4a160f5708bf0e4b
    >>> sus_update(num_rolls, 1, 3, make_test_dice(5)) # 1 and 5 are not sus, but 6 is!
    LOCKED: a1157827172ca94d

    """


@points(1)
def sus_fuss_examples():
    """
    >>> from hog import *
    >>> import tests.construct_check as test

    >>> num_factors(28)
    6

    >>> num_factors(64)
    7

    >>> num_factors(72)
    12

    >>> num_factors(97)
    2

    >>> num_factors(99)
    6

    >>> sus_points(1)
    1

    >>> sus_points(21)
    23

    >>> sus_points(25)
    29

    >>> sus_points(62)
    67

    >>> sus_points(64)
    64

    >>> sus_points(67)
    67

    >>> sus_points(75)
    75

    >>> sus_points(86)
    89

    >>> sus_points(100)
    100

    >>> simple_update(2, 5, 7, make_test_dice(2, 4))
    11
    >>> sus_update(2, 5, 7, make_test_dice(2, 4)) # is 11 a sus number?
    11

    >>> simple_update(0, 15, 37) # what happens when you roll 0 dice?
    21
    >>> sus_update(0, 15, 37) # is 21 a sus number?
    23

    >>> sus_update(3, 11, 12, make_test_dice(4, 5, 6))
    29

    >>> sus_update(2, 29, 17, make_test_dice(1, 3))
    30

    >>> sus_update(0, 41, 42)
    50

    >>> sus_update(0, 40, 22)
    47

    >>> sus_update(2, 56, 56, make_test_dice(4))
    64

    >>> import types
    >>> def imports():
    ...     for name, val in globals().items():
    ...         if isinstance(val, types.ModuleType):
    ...             yield val.__name__
    >>> list(imports()) # do NOT import any new modules!
    ['tests.construct_check', 'types']

    >>> import hog
    >>> def sus_points(score):
    ...     print("Called sus_points on", score)
    ...     return 9001
    ...
    >>> hog.sus_points, old_sus_points = sus_points, hog.sus_points
    >>> sus_update(2, 5, 7, make_test_dice(2, 4)) # Make sure you call sus_points!
    Called sus_points on 11
    9001
    >>> sus_update(0, 15, 37) # ... even when rolling 0 dice
    Called sus_points on 21
    9001

    """
