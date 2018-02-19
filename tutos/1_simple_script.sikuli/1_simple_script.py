# -*- coding:utf-8 -*-

"""

    tutos/1_simple_script.sikuli/1_simple_script.py

    Sikuli first script
    ===================

    see tutos/1_simple_script.md

    Scenario
    --------

    Open webbrowser
    Go to http://www.google.com
    search for 'Sikuli'
    wait first result

    Status
    ------

    OK
    date: 2/19/2018

    .. sectionauthor:: Adrian Pothuaud <adrianpothuaud2@gmail.com>

"""

from sikuli import *            # sikuli features

import webbrowser               # python web browser automation


# open google
webbrowser.open("http://www.google.com")
wait("google.png")
# type 'Sikuli'
click("google.png")
paste("Sikuli")
wait(0.5)
# search
Region(200, 200, 200, 200).getCenter().click()
wait(1)
click("search.png")
# wait result
wait("sikuli-script-home.png")
