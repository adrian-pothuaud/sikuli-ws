# -*- coding:utf-8 -*-

"""
ok 2/19/2018 - Windows
"""

import unittest
import datetime
import HTMLTestRunner
import testscontext
import path_utils


class PathUtilsTestCase(unittest.TestCase):

    def testParentDirname(self):
        if Env.isWindows():
            resp = path_utils.get_parent_dirname(os.path.join(r"C:/Users"), 1)
            self.assertEqual(resp, "C:/")
        else:
            resp = path_utils.get_parent_dirname(os.path.join(r"\usr\bin"), 1)
            self.assertEqual(resp, "\usr")

    def testAddExecPath(self):
        old_path = []
        for p in sys.path:
            old_path.append(p)
        if Env.isWindows():
            new_path = r"C:"
            path_utils.add_execution_path(new_path)
        else:
            new_path = r"\usr\bin"
            path_utils.add_execution_path(new_path)
        self.assertNotEqual(old_path, sys.path)
        self.assertNotEqual(len(old_path), len(sys.path))
        self.assertTrue(len(old_path) < len(sys.path))
        self.assertIn(new_path, sys.path)

    def testAddImagePath(self):
        old_path = []
        for p in getImagePath():
            old_path.append(p)
        if Env.isWindows():
            new_path = r"C:\Users"
            path_utils.add_image_path(new_path)
        else:
            new_path = r"\usr\bin\"
            path_utils.add_image_path(new_path)
        self.assertNotEqual(old_path, getImagePath())
        self.assertNotEqual(len(old_path), len(getImagePath()))
        self.assertTrue(len(old_path) < len(getImagePath()))
        self.assertIn(new_path, getImagePath())

if __name__ == '__main__':

    tests = unittest.TestLoader().loadTestsFromTestCase(PathUtilsTestCase)
    now = datetime.datetime.now()
    filename = "{}-{}-{}.{}h{}.html".format(
        now.year, now.month, now.day, now.hour, now.minute
    )
    with open(os.path.join(testscontext.outpath, 'test_reports', 'path_utils_tests', filename), 'w') as rf:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream = rf, description="Unit testing src/path_utils. Environment: {}.".format(Env.getOS()),
            title="Path utils", dirTestScreenshots=os.path.join(testscontext.outpath, 'test_reports', 'path_utils_tests', 'screenshots')
        )
        runner.run(tests)
