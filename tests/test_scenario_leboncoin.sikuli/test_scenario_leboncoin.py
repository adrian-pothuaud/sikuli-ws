# -*- coding:utf-8 -*-

"""
    Test Scenario: Leboncoin Login
    ==============================

    What is tested here ?
    ---------------------

    1. As an unregistered user I am unable to login
    2. As a visitor I am able to create an account
    3. As a registered user I am able to login

    Dependencies
    ------------

    Describe dependencies.
    Dependencies are important to be known as if the scenario fails,
    we should unit test the dependencies before giving a status of the application !

    - src/objects/Chrome.sikuli: Chrome Application Object

    Results:
    --------

    The results of these tests will be stored in:
    out/smoketests/sample

    .. sectionauthor:: Adrian Pothuaud <adrianpothuaud2@gmail.com>

"""

import unittest
import datetime
import HTMLTestRunner
import testscontext

# dependencies
# (those we should verify in case of failures)
import Chrome


class SampleTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.a = 'a'

    def testSampleFunction(self):
        self.assertTrue(isinstance(srcsample.sample_function_1('b'), dict))


if __name__ == '__main__':

    tests = unittest.TestLoader().loadTestsFromTestCase(SampleTestCase)
    now = datetime.datetime.now()
    filename = "{}-{}-{}.{}h{}.html".format(
        now.year, now.month, now.day, now.hour, now.minute
    )
    with open(os.path.join(testscontext.outpath, 'test_reports', 'srcsample_tests', filename), 'w') as rf:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream = rf, description="Unit testing src/srcsample. Environment: {}.".format(Env.getOS()),
            title="Sample", dirTestScreenshots=os.path.join(testscontext.outpath, 'test_reports', 'srcsample_tests')
        )
        runner.run(tests)
