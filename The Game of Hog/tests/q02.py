from pytest_grader import points


@points(1)
def boar_brawl():
    """
    >>> from hog import *
    >>> import tests.construct_check as test
    >>> boar_brawl(21, 46)
    LOCKED: 41011e381c5e4036
    >>> boar_brawl(52, 79)
    LOCKED: eabd690bddf54485
    >>> boar_brawl(0, 0)
    LOCKED: 2402241fe37bd084
    >>> boar_brawl(0, 5)
    LOCKED: 599e6738dd505c89
    >>> boar_brawl(5, 0)
    LOCKED: 4a6a864afbf8a43a
    >>> boar_brawl(2, 5)
    LOCKED: d115b8ed189038ac
    >>> boar_brawl(7, 2)
    LOCKED: 910eccb9a90e7218
    >>> boar_brawl(72, 29)
    LOCKED: 9458ecef951dd7f4

    """


@points(1)
def boar_brawl_examples():
    """
    >>> from hog import *
    >>> import tests.construct_check as test
    >>> boar_brawl(6, 10)
    15
    >>> boar_brawl(16, 27)
    12
    >>> boar_brawl(39, 71)
    6
    >>> boar_brawl(82, 115) # don't assume scores are below 100
    3
    >>> boar_brawl(99, 121) # don't assume scores are below 100
    21
    >>> boar_brawl(109, 99) # don't assume scores are below 100
    1

    >>> a = boar_brawl(42, 61)
    >>> a # check that the value is being returned, not printed
    12

    >>> boar_brawl(727, 939)
    12
    >>> # ban str and indexing and for statements and lists
    >>> test.check('hog.py', 'boar_brawl', ['Str', 'Slice', 'List', 'ListComp', 'Index', 'Subscript', 'For'])
    True

    """
