from pytest_grader import points


@points(0)
def memo_diff():
    r"""
    >>> from cats import minimum_mewtations, furry_fixes, autocorrect, lines_from_file
    >>> all_words = lines_from_file("data/words.txt")
    >>> common_words = lines_from_file("data/common_words.txt")
    >>> def my_decorator(func):
    ...   def wrapper():
    ...       print("Say Hello")
    ...       func()
    ...       print("Say Goodbye")
    ...   return wrapper

    >>> @my_decorator
    ... def say_hello():
    ...     print("Hello World")

    >>> say_hello()
    LOCKED: 4eb46254fe59b28b
    LOCKED: 3b4a43cadb6104f5
    LOCKED: 1ed58cceb8f41086
    >>> def magic_decorator(func):
    ...   def wrapper(x):
    ...     return func(x * 2)
    ...   return wrapper

    >>> @magic_decorator
    ... def myfunc(x):
    ...   return x * 3

    >>> print(myfunc(4))
    LOCKED: 21e9547f22f26373
    """


@points(0)
def memo_diff_examples():
    r"""
    >>> from cats import minimum_mewtations, furry_fixes, autocorrect, lines_from_file
    >>> all_words = lines_from_file("data/words.txt")
    >>> common_words = lines_from_file("data/common_words.txt")
    >>> big_limit = 10
    >>> minimum_mewtations.call_count = 0
    >>> minimum_mewtations("rlogcul", "logical", big_limit)    # rlogcul -> logcul -> logicul -> logical
    3
    >>> minimum_mewtations.call_count <= 350    # see if you removed redundant recursive calls
    True
    >>> minimum_mewtations.call_count = 0
    >>> minimum_mewtations("ckiteus", "kittens", big_limit)
    3
    >>> minimum_mewtations.call_count <= 320
    True
    >>> # check that you're only using the minimum_mewtations func
    >>> import trace, io
    >>> from contextlib import redirect_stdout
    >>> with io.StringIO() as buf, redirect_stdout(buf):
    ...     trace.Trace(trace=True).runfunc(minimum_mewtations, "abc", "def", 3)
    ...     output = buf.getvalue()
    >>> lines = [line for line in output.split('\n') if 'funcname' in line]
    >>> func_names = set([l.split(",")[1].split(":")[1].strip() for l in lines])
    >>> func_names == {'counted', 'minimum_mewtations', 'memoized'}   # make sure you are not using any helper functions
    True
    >>> minimum_mewtations.call_count = 0
    >>> autocorrect("woll", common_words, minimum_mewtations, 4)
    'well'
    >>> minimum_mewtations.call_count <= 72000    # minimum_mewtations should be memoized
    True
    >>> minimum_mewtations.call_count = 0
    >>> autocorrect("woll", common_words, furry_fixes, 4)
    'well'
    >>> minimum_mewtations.call_count
    0
    >>> minimum_mewtations.call_count = 0
    >>> autocorrect("woll", common_words, minimum_mewtations, 4)  # identical to the first call
    'well'
    >>> minimum_mewtations.call_count
    0
    >>> minimum_mewtations.call_count = 0
    >>> autocorrect("woll", common_words, minimum_mewtations, 4)
    'well'
    >>> minimum_mewtations.call_count
    0
    >>> minimum_mewtations.call_count = 0
    >>> autocorrect("woll", common_words, minimum_mewtations, 3)
    'well'
    >>> minimum_mewtations.call_count < 2500
    True
    >>> minimum_mewtations.call_count = 0
    >>> autocorrect("woll", all_words, minimum_mewtations, 2)
    'will'
    >>> minimum_mewtations.call_count < 2700000
    True
    """
