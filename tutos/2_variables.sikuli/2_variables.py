# -*- coding:utf-8 -*-

"""

    tutos/2_variables.sikuli/2_variables.py

    Sikuli tutorial n°2
    ===================

    see tutos/2_variables.md

    Scenario
    --------

    Open webbrowser
    Go to http://www.google.com
    search for 'Sikuli'
    wait first result

    Status
    ------

    OK
    date: 2/20/2018

    .. sectionauthor:: Adrian Pothuaud <adrianpothuaud2@gmail.com>

"""

from sikuli import *                        # sikuli features
import webbrowser                           # python web browser automation


url         = "http://www.google.com"       # reusable variables
google      = "google.png"
query       = "SikuliX"
topleft     = Region(200, 200, 200, 200)
search      = "search.png"
defaultWait = 0.5
result      = "sikuli-script-home.png"


webbrowser.open(url)                        # open an url
wait(google)

click(google)                               # type a query
paste(query)
wait(defaultWait)

topleft.getCenter().click()                 # search
wait(defaultWait)
click(search)

wait(result)                                # wait result
