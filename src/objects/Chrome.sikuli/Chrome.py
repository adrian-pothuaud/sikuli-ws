# -*- coding:utf-8 -*-

"""

"""

from sikuli import *

import os
import glob

import Browser

DEBUG = True


class Chrome(Browser.Browser):
    """

    """

    def __init__(self):
        if Env.isWindows():
            chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        elif Env.isMac():
            chrome_path = r"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        else:
            raise Exception("Unsupported OS")
        Browser.__init__(self, "google chrome", chrome_path)
        self.name = "google chrome"
        self.path = chrome_path

    def bookmark(self):
        """

        """
        click("bookmark_this_page.PNG")

    def clean_caches(self):
        """

        """
        if DEBUG:
            print("Cleaning Chrome caches")
        if Env.isWindows():
            if DEBUG:
                print("Env is WINDOWS")
            appdata = os.environ['APPDATA']
            localappdata = os.environ['LOCALAPPDATA']
            chromedata = os.path.join("Google", "Chrome", "User Data")
            for datadir in (appdata, localappdata):
                if DEBUG:
                    print("Cleaning dir {}".format(datadir))
                mydir = os.path.join(datadir, chromedata)
                if DEBUG:
                    print("mydir: {}".format(mydir))
                filelist = [ f for f in os.listdir(mydir) ]
                for f in filelist:
                    if DEBUG:
                        print("Looking at {}".format(f))
                    if os.path.isfile(f):
                        os.unlink(f)
                    elif os.path.isdir(f):
                        shutil.rmtree(f)
        elif Env.isMac():
            pass
        else:
            pass
