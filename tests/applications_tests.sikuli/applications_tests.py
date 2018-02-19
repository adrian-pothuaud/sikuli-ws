# -*- coding:utf-8 -*-

"""

"""

import unittest
import os
import datetime
import HTMLTestRunner
import testscontext
import applications

class ApplicationsTestCase(unittest.TestCase):

    def setUp(self):
        App.close('Google Chrome')

    def testLaunchChromeWithoutWaiting(self):
        applications.launch_app("google chrome", wait_img=False, timeout=10)

    def testLaunchChromeAndWait(self):
        applications.launch_app("google chrome", wait_img=True, timeout=10)


if __name__ == '__main__':

    tests = unittest.TestLoader().loadTestsFromTestCase(ApplicationsTestCase)
    now = datetime.datetime.now()
    filename = "{}-{}-{}.{}h{}.html".format(
        now.year, now.month, now.day, now.hour, now.minute
    )
    with open(os.path.join(testscontext.outpath, 'test_reports', 'applications_tests', filename), 'w') as rf:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream = rf, description="Unit testing src/applications. Environment: {}.".format(Env.getOS()), title="Applications"
        )
        runner.run(tests)
