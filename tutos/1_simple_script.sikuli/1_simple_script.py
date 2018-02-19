# -*- coding:utf-8 -*-

"""
Describe this module here ...
"""

from sikuli import *            # sikuli features

import webbrowser


webbrowser.open("http://www.google.com")
wait("google.png")
click("google.png")
paste("sikuli")
wait(0.5)
Region(200, 200, 200, 200).getCenter().click()
wait(1)
click("search.png")
wait("sikuli-script-home.png")
