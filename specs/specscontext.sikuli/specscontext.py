# -*- coding:utf-8 -*-

"""
This module is intended to allow src imports in any other module in specs

e.g: in specsample.sikuli/specsample.py write the following

import context



status: OK (02-19-2018)
test: run specsample
"""

from sikuli import *

import sys
import os

DEBUG = True

rootpath = os.path.dirname(os.path.dirname(getBundlePath()))
srcpath = os.path.join(rootpath, "src")
objpath = os.path.join(srcpath, "objects")

if DEBUG:
    print("Adding paths as a context...")

for path in (srcpath, objpath):
    if not path in sys.path:
        if DEBUG:
            print("adding {}".format(path))
        sys.path.append(path)
    else:
        if DEBUG:
            print("path {} already in sys.path".format(path))

if __name__ == '__main__':

    """
    src and objects paths should be in sys.path
    """

    print("sys.path now looks like:\n{")
    for path in sys.path:
        print("\t{},".format(path))
    print("}")
