Tests Folder
============

**Test modules are intended for :**
- **unit testing sources**
- **scenario testing applications**

Write new tests
---------------

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
**Don't forget to create out/test_reports/srcsample_tests folder**

:sunglasses:
