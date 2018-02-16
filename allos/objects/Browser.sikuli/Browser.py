# -*- coding:utf-8 -*-

'''Control Web Browsers within objects'''

from sikuli import *

import Application

class Browser(Application.Application):
    '''Web browser object'''
    def __init__(self, app_name, exec_path):
        '''Constructor, parameters name and path'''
        Application.__init__(self, app_name, exec_path)
    def new_tab(self, target_url = False):
        '''Open a new browser tab'''
        type('t', Key.CTRL)
        if target_url:
            wait(1)
            paste(target_url)
            type(Key.ENTER)
