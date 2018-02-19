# -*- coding:utf-8 -*-

'''Unit tests for allos/applications module'''

from sikuli import *

import os, sys, unittest, datetime, HTMLTestRunner

# find path of [ROOT]/allos folder
allos_path = this_path = getBundlePath()
for i in range(3):
    allos_path = os.path.dirname(allos_path)
allos_path = os.path.join(allos_path, "allos")
# add it to path
if not allos_path in sys.path:
    sys.path.append(allos_path)
# import applications module
import applications, path_utils

class ApplicationsTestCase(unittest.TestCase):
    def testLaunchChromeWithoutWaiting(self):
        applications.launch_app("google chrome", wait_img=False, timeout=10)
    def testLaunchChromeAndWait(self):
        applications.launch_app("google chrome", wait_img=True, timeout=10)

tests = unittest.TestLoader().loadTestsFromTestCase(ApplicationsTestCase)
out_folder = os.path.join(
    path_utils.get_ws_root_path(),
    "out",
    "test_reports",
    "allos",
    "applications_tests"
)
now = datetime.datetime.now()
filename = "{}-{}-{}.{}h{}.html".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute
)
with open(os.path.join(out_folder, filename), 'w') as rf:
    runner = HTMLTestRunner.HTMLTestRunner(
        stream = rf
    )
    runner.run(tests)
