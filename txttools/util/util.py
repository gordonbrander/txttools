def isep(strings, sep):
    """
    Given an iterable of strings, return an iterable of strings with
    sep in-between.
    """
    i = 0
    for s in strings:
        if i > 0:
            yield sep
        yield s
        i = i + 1