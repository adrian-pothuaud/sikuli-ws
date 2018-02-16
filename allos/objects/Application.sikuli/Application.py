# -*- coding:utf-8 -*-

'''Conrol Applications within objects'''

from sikuli import *

class Application:
    '''Generic Application'''
    def __init__(self, app_name, exec_path):
        '''Constructor, parameters: name and path'''
        print("building an app...")
        self.name = app_name
        self.path = exec_path
    def __str__(self):
        return "Application '{}'".format(self.name)
    def open(self):
        print('opening {}'.format(self))
        self.app = App(self.name)
        if self.app.isRunning():
            # app is running
            print('app is running')
            self.appInst = self.app
        else:
            # app is not running
            print('app is not running')
            self.app.open(self.path)
        wait(2)
        print('app should be openned')


if __name__ == '__main__':

    a = App('Firefox')
    if not a.isRunning():
        a.open(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
    a = switchApp('Firefox')
