# -*- coding:utf-8 -*-

'''Unit tests for allos/pah_utils module'''

from sikuli import *

import os, sys, unittest

# find path of [ROOT]/allos folder
allos_path = this_path = getBundlePath()
for i in range(3):
    allos_path = os.path.dirname(allos_path)
allos_path = os.path.join(allos_path, "allos")
# add it to path
if not allos_path in sys.path:
    sys.path.append(allos_path)
# import path_utils module
import path_utils

class PathUtilsTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        if Env.isWindows():
            self.cur_env = 'win'
        elif Env.isMac() or Env.isLinux():
            self.cur_env = 'uni'
        else:
            raise Exception('Current OS is not supported')

    def testParentDirname(self):
        if self.cur_env == 'win':
            resp = path_utils.get_parent_dirname(os.path.join(r"C:/Users"), 1)
            self.assertEqual(resp, "C:/")
        else:
            resp = path_utils.get_parent_dirname(os.path.join(r"\usr\bin"), 1)
            self.assertEqual(resp, "\usr")

    def testAddExecPath(self):
        old_path = []
        for p in sys.path:
            old_path.append(p)
        if self.cur_env == 'win':
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
        if self.cur_env == 'win':
            new_path = r"C:\Users"
            path_utils.add_image_path(new_path)
        else:
            new_path = r"\usr\bin\"
            path_utils.add_image_path(new_path)
        self.assertNotEqual(old_path, getImagePath())
        self.assertNotEqual(len(old_path), len(getImagePath()))
        self.assertTrue(len(old_path) < len(getImagePath()))
        self.assertIn(new_path, getImagePath())

tests = unittest.TestLoader().loadTestsFromTestCase(PathUtilsTestCase)
runner = unittest.TextTestRunner()
runner.run(tests)
