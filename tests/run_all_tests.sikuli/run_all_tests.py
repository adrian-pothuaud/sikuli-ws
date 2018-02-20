# -*- coding:utf-8 -*-

"""
    Run every test scripts in tests folder !
"""

from sikuli import *

import glob

DEBUG = True

scriptslist = glob.glob(os.path.join(os.path.dirname(getBundlePath()), "*.sikuli"))
if DEBUG:
    print("scripts list:")
    for s in scriptslist:
        print("\t{}".format(s))

for script in scriptslist:
    if "run_all" not in script and "context" not in script:
        if DEBUG:
            print("Script: {} is going to be executed...".format(script))
        runScript(script)
if DEBUG:
    print("All scripts have been launched ! Bye Bye ...")
