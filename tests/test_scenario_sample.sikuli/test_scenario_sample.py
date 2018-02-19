# -*- coding:utf-8 -*-

"""
    Test Scenario: Sample
    ==============================

    What is tested here ?
    ---------------------

    1. As a visitor I can go to MySampleApp
    2. As a visitor I can search anything

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


# define test classes here
# scenario 1
class ICanGoToMySampleApp(unittest.TestCase):

    def testIGoNowhereItIsASample(self):
        self.assertTrue(1 + 2 == 3)

# scenario 2
class ICanSearchAnything(unittest.TestCase):

    def testISearchNothingItIsASample(self):
        self.assertNotIn(4, (1, 2, 3))


if __name__ == '__main__':

    test_list = unittest.TestSuite()

    for tc in (ICanGoToMySampleApp, ICanSearchAnything):
        tests = unittest.TestLoader().loadTestsFromTestCase(tc)
        test_list.addTests(tests)

    now = datetime.datetime.now()
    filename = "{}-{}-{}.{}h{}.html".format(
        now.year, now.month, now.day, now.hour, now.minute
    )
    with open(os.path.join(testscontext.outpath, 'smoketests', 'sample', filename), 'w') as rf:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream = rf, description="Test Scenario: Sample. Environment: {}.".format(Env.getOS()),
            title="Sample", dirTestScreenshots=os.path.join(testscontext.outpath, 'smoketests', 'sample', 'screenshots')
        )
        runner.run(test_list)
