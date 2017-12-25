'''
Utility to sort nicely -- the way a human might -- so "10. Hello"
comes after "1. Hello"
'''

import re


def _tryint(s):
    '''
    Takes a string. Converts it to an integer if it can. Otherwise,
    returns the string.
    '''
    try:
        return int(s)
    except:
        return s


def _alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    return [_tryint(c) for c in re.split('([0-9]+)', s)]


def sort_nicely(l):
    """
    Sort the given list in the way that humans expect.
    """
    l.sort(key=_alphanum_key)
