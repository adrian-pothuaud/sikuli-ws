# -*- coding:utf-8 -*-

'''Control Google Chrome within objects'''

from sikuli import *

from Browser import Browser
from Application import Application

class Chrome(Browser):
    '''Google Chrome'''
    def __init__(self):
        if Env.isWindows():
            chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        elif Env.isMac():
            chrome_path = r"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        else:
            raise Exception("Unsupported OS")
        Application.__init__(self, "google chrome", chrome_path)
    def bookmark(self):
        click("bookmark_this_page.PNG")

if __name__ == '__main__':

    c = Chrome()
    c.open()
