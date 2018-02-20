# -*- coding:utf-8 -*-

"""
file: jython/src/osx/Spotlight.py

Spotlight Object
================

Description
-----------

"""

from sikuli import *

DEBUG = True

root = os.path.dirname(os.path.dirname(os.path.dirname(getBundlePath())))
if DEBUG:
    print("module's root path: {}".format(root))
# noinspection SpellCheckingInspection
img_lib = os.path.join(root, "imgs", "spotlight")
if DEBUG:
    print("module's image path: {}".format(img_lib))
addImagePath(img_lib)


class Spotlight:

    def __init__(self):
        pass

    def open(self):
        """

        :return:
        """
        type(Key.SPACE, Key.CMD)
        wait("search_icon.png", 10).higlight(1)
        if DEBUG:
            print("Spotlight is open")


s = Spotlight()
s.open()
