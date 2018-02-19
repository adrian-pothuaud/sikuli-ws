# -*- coding:utf-8 -*-

"""

    The '''path_utils''' module
    ===========================

    Use it to import sikuli paths functions.

    Module content
    --------------

    - add_execution_path
    - add_image_path
    - get_parent_dirname
    - print_execution_path
    - print_image_path

    Module state
    ------------
    status: OK(02-18-2018)
    test: run specs/paths.sikuli
    unit tests:
        - run tests/path_utils_tests.sikuli
        - results: out/test_reports/path_utils_tests

    ..todo:: Sort functions in alphabetical order
    .. sectionauthor:: Adrian Pothuaud <adrianpothuaud2@gmail.com>

"""

from sikuli import *

import sys, os

DEBUG = True


def add_execution_path(new_path):
    """
    Add a path to sys.path

    With a given path
    - verify if path already in sys.path
    - if not add it
    With a given list of paths
    - do the same for each path

    :param path: a path or a list of paths to add
    :type path: str or unicode or list
    :return: Nothing
    :rtype: None or ValueError if path is neither str nor unicode

    """
    if isinstance(new_path, str) or isinstance(new_path, unicode):
        new_path = [new_path]
    if isinstance(new_path, list):
        for p in new_path:
            if DEBUG:
                print("Trying to add {} to execution path".format(p))
            if not p in sys.path:
                sys.path.append(p)
                if DEBUG:
                    print("Path {} added !".format(p))
            else:
                if DEBUG:
                    print("Path {} already in execution path ! Nothing done...".format(p))
    else:
        raise ValueError("'new_path' parameter : {}, is neither str nor list !".format(new_path))

def add_image_path(new_path):
    """
    Add a path to sikuli image path

    With a given path
    - verify if path already in sys.path
    - if not add it
    With a given list of paths
    - do the same for each path
    Adding a path to image path will not add it into sys.path.

    :param path: a path or a list of paths to add
    :type path: str or unicode or list
    :return: Nothing
    :rtype: None or ValueError if path is neither str nor unicode

    """
    if isinstance(new_path, str) or isinstance(new_path, unicode):
        new_path = [new_path]
    if isinstance(new_path, list):
        for p in new_path:
            if DEBUG:
                print("Trying to add {} to image path".format(p))
            if not p in getImagePath():
                addImagePath(p)
                if DEBUG:
                    print("Path {} added !".format(p))
            else:
                if DEBUG:
                    print("Path {} already in image path ! Nothing done...".format(p))
    else:
        raise ValueError("'new_path' parameter : {}, is neither str nor list !".format(new_path))

def get_parent_dirname(path, level = 1):
    """
    Get parent directory with level of relationship.

    With a given path
    and a given level 'l' (default 1)
    returns pdir where:
    pdir (level: l)
    |_ (level: l-1)
    [...]
    |__________ path (level: 0)

    :param path: a path or a list of paths to add
    :param level: level of relationship. Default:1.
    :type path: str or unicode
    :type level: int
    :return: path to the parent directory
    :rtype: unicode

    """
    if DEBUG:
        print("Finding parent level {} of path {}".format(level, path))
    parent = path
    for i in range(level):
        parent = os.path.dirname(parent)
    return parent

def print_execution_path():
    """
    Print execution path to the stdout

    """
    print("Actual execution path is :\n{")
    for p in sys.path:
        print("\t{},".format(p))
    print("}")

def print_image_path():
    """
    Print image path to the stdout

    """
    print("Actual image path is :\n{")
    for p in getImagePath():
        print("\t{},".format(p))
    print("}")
