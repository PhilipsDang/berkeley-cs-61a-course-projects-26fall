from pytest_grader import points


@points(1)
def roll_dice_with_test_dice():
    """
    >>> from hog import *
    >>> roll_dice(5, make_test_dice(4, 2, 3, 3, 4, 1))
    LOCKED: 81ace59c3f3e51fd

    >>> roll_dice(2, make_test_dice(1))
    LOCKED: 789e457faa06a252

    >>> dice = make_test_dice(5, 4, 3, 2, 1)
    >>> roll_dice(1, dice)    # Outcomes: (5)
    LOCKED: 91711180949de266
    >>> roll_dice(4, dice)    # Outcomes: (4, 3, 2, 1)
    LOCKED: 0baaa547570b10e9
    >>> roll_dice(2, dice)    # Outcomes: (5, 4)
    LOCKED: 809283d3a9d23b96
    >>> roll_dice(6, dice)    # Outcomes: (3, 2, 1, 5, 4, 3)
    LOCKED: ba9d37f512d15ca4
    >>> roll_dice(3, dice)    # Outcomes: <you figure it out>
    LOCKED: 1885ea449ac75b10
    >>> roll_dice(2, dice)    # Outcomes: <you figure it out>
    LOCKED: 9b7de13eee4f6bf6
    """


@points(1)
def roll_dice():
    """
    >>> from hog import *
    >>> import tests.construct_check as test
    >>> roll_dice(2, make_test_dice(4, 6, 1))
    10

    >>> roll_dice(3, make_test_dice(4, 6, 1))
    1

    >>> roll_dice(4, make_test_dice(2, 2, 3))
    9

    >>> a = roll_dice(4, make_test_dice(1, 2, 3))
    >>> a # check that the value is being returned, not printed
    1

    >>> counted_dice = make_test_dice(4, 1, 2, 6)
    >>> roll_dice(3, counted_dice)
    1
    >>> # Make sure you call dice exactly num_rolls times!
    >>> # If you call it fewer or more than that, it won't be at the right spot in the cycle for the next roll
    >>> # Note that a return statement within a loop ends the loop
    >>> roll_dice(1, counted_dice)
    6

    >>> roll_dice(9, make_test_dice(6))
    54
    >>> roll_dice(7, make_test_dice(2, 2, 2, 2, 2, 2, 1))
    1

    >>> # ban str and indexing and for statements and lists
    >>> test.check('hog.py', 'roll_dice', ['Str', 'Slice', 'List', 'ListComp', 'Index', 'Subscript', 'For'])
    True

    >>> # Randomly generated tests
    >>> dice = make_test_dice(2, 4, 3, 5, 2, 2)
    >>> roll_dice(4, dice)
    14
    >>> roll_dice(4, dice)
    10
    >>> roll_dice(3, dice)
    10


    >>> dice = make_test_dice(1, 4, 5, 4, 3)
    >>> roll_dice(2, dice)
    1
    >>> roll_dice(1, dice)
    5
    >>> roll_dice(4, dice)
    1
    >>> roll_dice(3, dice)
    12

    >>> dice = make_test_dice(5, 2)
    >>> roll_dice(4, dice)
    14
    >>> roll_dice(3, dice)
    12

    >>> dice = make_test_dice(3, 1, 4, 1, 3, 4)
    >>> roll_dice(4, dice)
    1
    >>> roll_dice(1, dice)
    3
    >>> roll_dice(2, dice)
    7
    >>> roll_dice(3, dice)
    1

    >>> dice = make_test_dice(1,)
    >>> roll_dice(3, dice)
    1
    >>> roll_dice(2, dice)
    1
    >>> roll_dice(5, dice)
    1
    >>> roll_dice(1, dice)
    1

    >>> dice = make_test_dice(4,)
    >>> roll_dice(4, dice)
    16

    >>> dice = make_test_dice(2, 3, 5)
    >>> roll_dice(1, dice)
    2
    >>> roll_dice(5, dice)
    18
    >>> roll_dice(3, dice)
    10

    >>> dice = make_test_dice(1, 5, 4)
    >>> roll_dice(2, dice)
    1
    >>> roll_dice(1, dice)
    4
    >>> roll_dice(5, dice)
    1

    >>> dice = make_test_dice(2,)
    >>> roll_dice(4, dice)
    8

    >>> dice = make_test_dice(1,)
    >>> roll_dice(2, dice)
    1

    >>> dice = make_test_dice(3, 1, 3)
    >>> roll_dice(2, dice)
    1

    >>> dice = make_test_dice(4, 5)
    >>> roll_dice(4, dice)
    18
    >>> roll_dice(2, dice)
    9
    >>> roll_dice(5, dice)
    22

    >>> dice = make_test_dice(1, 4)
    >>> roll_dice(3, dice)
    1
    >>> roll_dice(4, dice)
    1

    >>> dice = make_test_dice(1, 1, 3, 5)
    >>> roll_dice(3, dice)
    1
    >>> roll_dice(1, dice)
    5
    >>> roll_dice(5, dice)
    1

    >>> dice = make_test_dice(3, 2, 1, 2, 3, 2)
    >>> roll_dice(2, dice)
    5

    >>> dice = make_test_dice(2, 5, 1, 3)
    >>> roll_dice(4, dice)
    1
    >>> roll_dice(4, dice)
    1

    >>> dice = make_test_dice(5, 4, 1, 4)
    >>> roll_dice(5, dice)
    1
    >>> roll_dice(3, dice)
    1

    >>> dice = make_test_dice(4, 5)
    >>> roll_dice(2, dice)
    9
    >>> roll_dice(4, dice)
    18
    >>> roll_dice(5, dice)
    22
    >>> roll_dice(3, dice)
    14

    >>> dice = make_test_dice(3, 5, 1, 4, 3)
    >>> roll_dice(1, dice)
    3

    >>> dice = make_test_dice(3, 1, 5, 2, 5, 3)
    >>> roll_dice(1, dice)
    3
    >>> roll_dice(2, dice)
    1
    >>> roll_dice(4, dice)
    13
    >>> roll_dice(4, dice)
    1

    >>> dice = make_test_dice(2,)
    >>> roll_dice(1, dice)
    2
    >>> roll_dice(4, dice)
    8

    >>> dice = make_test_dice(2, 3)
    >>> roll_dice(4, dice)
    10

    >>> dice = make_test_dice(3, 3, 5, 5, 1, 2)
    >>> roll_dice(3, dice)
    11
    >>> roll_dice(3, dice)
    1

    >>> dice = make_test_dice(3,)
    >>> roll_dice(4, dice)
    12
    >>> roll_dice(1, dice)
    3

    >>> dice = make_test_dice(5, 4, 1, 3)
    >>> roll_dice(4, dice)
    1

    >>> dice = make_test_dice(5, 3, 2, 1)
    >>> roll_dice(4, dice)
    1
    >>> roll_dice(4, dice)
    1
    >>> roll_dice(3, dice)
    10

    >>> dice = make_test_dice(3, 2, 2)
    >>> roll_dice(3, dice)
    7
    >>> roll_dice(1, dice)
    3
    >>> roll_dice(3, dice)
    7
    >>> roll_dice(5, dice)
    11

    >>> dice = make_test_dice(1, 3, 1, 5, 3, 3)
    >>> roll_dice(4, dice)
    1
    >>> roll_dice(4, dice)
    1

    >>> dice = make_test_dice(1,)
    >>> roll_dice(2, dice)
    1
    >>> roll_dice(2, dice)
    1
    >>> roll_dice(4, dice)
    1
    >>> roll_dice(4, dice)
    1

    >>> dice = make_test_dice(1, 4)
    >>> roll_dice(1, dice)
    1
    >>> roll_dice(4, dice)
    1
    >>> roll_dice(3, dice)
    1
    >>> roll_dice(2, dice)
    1

    >>> dice = make_test_dice(5, 2, 2, 3, 2, 5)
    >>> roll_dice(3, dice)
    9
    >>> roll_dice(3, dice)
    10
    >>> roll_dice(5, dice)
    14

    >>> dice = make_test_dice(1, 2, 3, 2, 4)
    >>> roll_dice(5, dice)
    1
    >>> roll_dice(2, dice)
    1

    >>> dice = make_test_dice(5, 3)
    >>> roll_dice(3, dice)
    13
    >>> roll_dice(1, dice)
    3

    >>> dice = make_test_dice(3, 3)
    >>> roll_dice(2, dice)
    6
    >>> roll_dice(1, dice)
    3
    >>> roll_dice(1, dice)
    3

    >>> dice = make_test_dice(1, 2, 1, 3)
    >>> roll_dice(4, dice)
    1

    >>> dice = make_test_dice(1, 2, 3, 2)
    >>> roll_dice(4, dice)
    1
    >>> roll_dice(4, dice)
    1
    >>> roll_dice(2, dice)
    1

    >>> dice = make_test_dice(1, 2, 3, 4, 1, 2)
    >>> roll_dice(5, dice)
    1
    >>> roll_dice(1, dice)
    2

    >>> dice = make_test_dice(3,)
    >>> roll_dice(3, dice)
    9
    >>> roll_dice(4, dice)
    12
    >>> roll_dice(4, dice)
    12

    >>> dice = make_test_dice(2, 5, 3, 3)
    >>> roll_dice(1, dice)
    2
    >>> roll_dice(2, dice)
    8
    >>> roll_dice(4, dice)
    13
    >>> roll_dice(2, dice)
    5

    >>> dice = make_test_dice(3,)
    >>> roll_dice(2, dice)
    6
    >>> roll_dice(2, dice)
    6

    >>> dice = make_test_dice(1, 3, 5, 4, 3)
    >>> roll_dice(3, dice)
    1
    >>> roll_dice(1, dice)
    4
    >>> roll_dice(4, dice)
    1

    >>> dice = make_test_dice(5, 4, 5, 1, 4, 5)
    >>> roll_dice(2, dice)
    9
    >>> roll_dice(5, dice)
    1

    >>> dice = make_test_dice(4,)
    >>> roll_dice(2, dice)
    8
    >>> roll_dice(3, dice)
    12
    >>> roll_dice(1, dice)
    4

    >>> dice = make_test_dice(1,)
    >>> roll_dice(4, dice)
    1
    >>> roll_dice(1, dice)
    1
    >>> roll_dice(2, dice)
    1

    >>> dice = make_test_dice(1, 1, 5, 5, 5)
    >>> roll_dice(4, dice)
    1
    >>> roll_dice(1, dice)
    5
    >>> roll_dice(1, dice)
    1

    >>> dice = make_test_dice(5, 5, 2, 2, 1, 3)
    >>> roll_dice(2, dice)
    10
    >>> roll_dice(5, dice)
    1
    >>> roll_dice(2, dice)
    7
    >>> roll_dice(2, dice)
    1

    >>> dice = make_test_dice(5,)
    >>> roll_dice(4, dice)
    20
    >>> roll_dice(4, dice)
    20
    >>> roll_dice(5, dice)
    25

    >>> dice = make_test_dice(1, 2, 2, 5, 4)
    >>> roll_dice(4, dice)
    1
    >>> roll_dice(5, dice)
    1
    >>> roll_dice(1, dice)
    4

    >>> dice = make_test_dice(1, 3)
    >>> roll_dice(5, dice)
    1

    >>> dice = make_test_dice(3, 3)
    >>> roll_dice(1, dice)
    3
    >>> roll_dice(4, dice)
    12
    >>> roll_dice(5, dice)
    15
    """


