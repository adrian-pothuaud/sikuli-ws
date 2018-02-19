# -*- coding: utf-8 -*-

'''Custom wait loops and image verification functions'''

from sikuli import *

def wait_all(img_list):
    '''Wait for a list of images to be present, returns a list with the matchs'''
    match_list = [None] * len(img_list)
    for i in img_list:
        if exists(i):
            match_list[img_list.index(i)] = wait(i)
    return match_list
