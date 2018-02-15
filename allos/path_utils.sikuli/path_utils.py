# -*- coding:utf-8 -*-

'''
Reusable functions to play with execution path and image path of Sikuli
'''

from sikuli import *

import sys, os

import settings

def get_ws_root_path():
    '''Returns path to the Sikuli workspace'''
    path = getBundlePath()
    while not settings.root_name in path.split(os.sep)[-1]:
        path = get_parent_dirname(path)
    return path

def get_parent_dirname(path, level = 1):
    '''return the parent of path'''
    parent = path
    for i in range(level):
        parent = os.path.dirname(parent)
    return parent

def print_execution_path():
    '''print execution path'''
    print("\nActual execution path is :\n{")
    for p in sys.path:
        print("\t{},".format(p))
    print("}\n")

def add_execution_path(new_path):
    '''add new path(s) to execution'''
    if isinstance(new_path, str) or isinstance(new_path, unicode):
        new_path = [new_path]
    if isinstance(new_path, list):
        for p in new_path:
            print("\nTrying to add {} to execution path".format(p))
            if not p in sys.path:
                sys.path.append(p)
                print("PATH ADDED !\n")
            else:
                print("ALREADY THERE ! nothing done\n")
    else:
        raise ValueError("'new_path' parameter : {}, is neither str nor list !".format(new_path))

def set_execution_path(path):
    '''USE WITH CAUTION: set execution path to the given path'''
    pass

def print_image_path():
    '''print image path'''
    print("\nActual image path is :\n{")
    for p in getImagePath():
        print("\t{},".format(p))
    print("}\n")

def add_image_path(new_path):
    '''add new path(s) to image path'''
    if isinstance(new_path, str) or isinstance(new_path, unicode):
        new_path = [new_path]
    if isinstance(new_path, list):
        for p in new_path:
            print("\nTrying to add {} to image path".format(p))
            if not p in getImagePath():
                addImagePath(p)
                print("PATH ADDED !\n")
            else:
                print("ALREADY THERE ! nothing done\n")
    else:
        raise ValueError("'new_path' parameter : {}, is neither str nor list !".format(new_path))

def set_image_path(path):
    '''USE WITH CAUTION: set image path to the given path'''
    pass

if __name__ == '__main__':

    print(get_ws_root_path())