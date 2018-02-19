# -*- coding: utf-8 -*-

"""
    The ``image_utils`` module
    ======================

    Use it to import image utility functions.

    Module content
    --------------

    - wait_all

    Module state
    ------------
    status: ?
    unit tests:
        - run tests/image_utils_tests.sikuli
        - results: out/test_reports/image_utils_tests

    .. sectionauthor:: Adrian Pothuaud <adrianpothuaud2@gmail.com>
    .. todo:: use screenshots for unit tests

"""

from sikuli import *

DEBUG = True

class NotAllImagesfound(Exception):
    pass

def wait_all(img_list):
    """
    Wait for all images in a list

    :param img_list: A list of images.
    :type img_list: list of str
    :return: A list of matchs.
    :rtype: list

    """
    if DEBUG:
        print("WAIT for all images in:")
        for img in img_list:
            print("\t{}".format(img))
    match_list = [None] * len(img_list)
    for i in img_list:
        if exists(i):
            match_list[img_list.index(i)] = wait(i)
    if not len(img_list) == len(match_list):
        raise NotAllImagesfound("images: {}, Matchs: {}".format(img_list, match_list))
    return match_list
