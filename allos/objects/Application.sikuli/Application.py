# -*- coding:utf-8 -*-

'''Conrol Applications within objects'''

class Application:
    '''Generic Application'''
    def __init__(self, app_name, exec_path):
        '''Constructor, parameters: name and path'''
        self.name = app_name
        self.path = exec_path
    def __str__(self):
        return "Application '{}'".format(self.name)
    def open(self):
        App.open(self.path)
