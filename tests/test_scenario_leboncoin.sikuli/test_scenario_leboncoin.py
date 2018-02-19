# -*- coding:utf-8 -*-

"""
    Test Scenario: Leboncoin
    ==============================

    What is tested here ?
    ---------------------

    1. As a visitor I can create an account
    2. As a user I can login
    3. As an unregistered user I can't login

    Dependencies
    ------------

    Describe dependencies.
    Dependencies are important to be known as if the scenario fails,
    we should unit test the dependencies before giving a status of the application !

    - src/objects/Chrome.sikuli: Chrome Application Object

    Results:
    --------

    The results of these tests will be stored in:
    out/smoketests/leboncoin

    .. sectionauthor:: Adrian Pothuaud <adrianpothuaud2@gmail.com>

"""

import unittest
import datetime
import HTMLTestRunner
import testscontext

# dependencies
# (those we should verify in case of failures)
import Chrome


# define test classes here
# scenario 1
class ICanCreateAnAccount(unittest.TestCase):

    def testIGoNowhereItIsASample(self):
        self.assertTrue(1 + 2 == 3)

# scenario 2
class ICanLoginWithValidUser(unittest.TestCase):

    def testISearchNothingItIsASample(self):
        self.assertNotIn(4, (1, 2, 3))

# scenario 3
class ICannotLoginWithInvalidUser(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.user = {
            "username": "unregistered123456",
            "email": "unregistered123456@test.com",
            "password": "unregistered123456"
        }
        self.chrome = Chrome()


if __name__ == '__main__':

    test_list = unittest.TestSuite()

    for tc in (ICanCreateAnAccount, ICanLoginWithValidUser, ICannotLoginWithInvalidUser):
        tests = unittest.TestLoader().loadTestsFromTestCase(tc)
        test_list.addTests(tests)

    now = datetime.datetime.now()
    filename = "{}-{}-{}.{}h{}.html".format(
        now.year, now.month, now.day, now.hour, now.minute
    )
    with open(os.path.join(testscontext.outpath, 'smoketests', 'leboncoin', filename), 'w') as rf:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream = rf, description="Test Scenario: Leboncoin login. Environment: {}.".format(Env.getOS()),
            title="Leboncoin", dirTestScreenshots=os.path.join(testscontext.outpath, 'smoketests', 'leboncoin', 'screenshots')
        )
        runner.run(test_list)
