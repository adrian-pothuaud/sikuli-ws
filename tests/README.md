Tests Folder
============

**Test modules are intended for :**
- **unit testing sources**
- **scenario testing applications**

Write new unit tests
--------------------

##### *Follow below instructions*

### Script template

**Use this template and write your code.**

    # -*- coding:utf-8 -*-

    """
    ok 2/19/2018 - Windows
    """

    import unittest
    import datetime
    import HTMLTestRunner
    import testscontext
    import srcsample


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

**Create unit tests for any sources.**
**Don't forget to create out/test_reports/srcsample_tests and out/test_reports/srcsample_tests/screenshots folders**

:sunglasses:

Write new test scenario
-----------------------

##### *Follow below instructions*

### Script template

**Use this template and write your code.**

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

**Don't forget to create out/smoketests/sample and out/smoketests/sample/screenshots folders**
