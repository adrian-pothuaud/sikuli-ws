# -*- coding:utf-8 -*-

'''Unit tests for allos/html_utils module'''

from sikuli import *

import os, sys, unittest, glob

# find path of [ROOT]/allos folder
allos_path = this_path = getBundlePath()
for i in range(3):
    allos_path = os.path.dirname(allos_path)
allos_path = os.path.join(allos_path, "allos")
# add it to path
if not allos_path in sys.path:
    sys.path.append(allos_path)
# import path_utils module
import html_utils

class HTMLUtilsTestCase(unittest.TestCase):
    def testHelloWorld(self):
        new_file = os.path.join(getBundlePath(), "out", "hello.html")
        html_utils.hello_world(new_file)
        self.assertIn(
            new_file,
            glob.glob(
                "{}{}*.html".format(
                    os.path.join(
                        getBundlePath(),
                        "out"
                    ),
                    os.sep
                )
            )
        )

tests = unittest.TestLoader().loadTestsFromTestCase(HTMLUtilsTestCase)
runner = unittest.TextTestRunner()
runner.run(tests)
