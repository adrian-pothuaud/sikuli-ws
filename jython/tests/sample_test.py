# -*- coding:utf-8 -*-

# noinspection PyUnresolvedReferences
# noinspection reason: context import is doing stuff
import context
# noinspection PyUnresolvedReferences
# noinspection reason: context import is doing stuff
import sample_src
from HtmlTestRunner import HTMLTestRunner
import unittest
import os


class SampleTestCase(unittest.TestCase):

    @staticmethod
    def testHelloSikuli():
        sample_src.say_hello_sikuli()


if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(SampleTestCase)

    runner = HTMLTestRunner(
        output=os.path.join(context.out_path, "tests", "sample"),
        report_title='Sample Test Report'
    )

    runner.run(suite)
