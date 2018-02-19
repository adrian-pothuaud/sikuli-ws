# -*- coding:utf-8 -*-

"""
ok 2/19/2018 - Windows
"""

import unittest
import os
import glob
import datetime
import HTMLTestRunner
import testscontext
import generate


class GenerateTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.mydir = getBundlePath()
        self.testScript = os.path.join(getBundlePath(), "GenerateTestCase.sikuli")
        self.testPyScript = os.path.join(getBundlePath(), "GenerateTestCase.sikuli", "GenerateTestCase.py")
        if len(glob.glob(os.path.join(self.testScript, "*.sikuli"))):
            filelist = [ f for f in os.listdir(mydir) ]
            for f in filelist:
                os.remove(os.path.join(mydir, f))
            os.rmdir(mydir)
        generate.create_sikuli_script(self.testScript, [r"# auto generated for test purpose"])

    def testGenerateContent(self):
        lines = []
        with open(self.testPyScript, 'r') as f:
            self.assertIn("# auto generated for test purpose\n", f.readlines())

    def testGenerateFiles(self):
        filelist = [ f for f in os.listdir(self.testScript) if f.endswith('.py') ]
        self.assertEquals(len(filelist), 1)
        filelist = [ f for f in os.listdir(self.testScript) if f.endswith('.html') ]
        self.assertEquals(len(filelist), 1)


if __name__ == '__main__':

    tests = unittest.TestLoader().loadTestsFromTestCase(GenerateTestCase)
    now = datetime.datetime.now()
    filename = "{}-{}-{}.{}h{}.html".format(
        now.year, now.month, now.day, now.hour, now.minute
    )
    with open(os.path.join(testscontext.outpath, 'test_reports', 'generate_tests', filename), 'w') as rf:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream = rf, description="Unit testing src/generate. Environment: {}.".format(Env.getOS()),
            title="Generate", dirTestScreenshots=os.path.join(testscontext.outpath, 'test_reports', 'generate_tests', 'screenshots')
        )
        runner.run(tests)
