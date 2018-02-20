# -*- coding:utf-8 -*-

# noinspection PyUnresolvedReferences
# noinspection reason: context import is doing stuff
import context
# noinspection PyUnresolvedReferences
# noinspection reason: context import is doing stuff
import sample_src
import unittest


class SampleTestCase(unittest.TestCase):

    @staticmethod
    def testHelloSikuli():
        sample_src.say_hello_sikuli()


if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(SampleTestCase)
    runner = unittest.TextTestRunner()
    runner.run(suite)
