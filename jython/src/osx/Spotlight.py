# -*- coding:utf-8 -*-

"""
file: jython/src/osx/Spotlight.py

Spotlight Object
================

Description
-----------

"""

from sikuli import *

import os

DEBUG = True

if DEBUG:
    print("RUN THIS SCRIPT FROM sikuli-ws/jtyhon/")
root = os.getcwd()
if DEBUG:
    print("module's root path: {}".format(root))
def getImg(path):
    """

    """
    img_lib = os.path.join(root, "imgs", "osx", "spotlight")
    return os.path.join()


class Spotlight:

    def __init__(self):
        self.search_icon = os.path.join()

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
