# -*- coding:utf-8 -*-

"""
	file: tests/testrunner.sikuli/testrunner.py

	Test runner
	===========

	Run a test given in sys.argv
	With runner given in sys.argv

	Usage
	-----
	runsikulix -r tests/testrunner.sikuli --args testscript testclass [testrunnerType]

	Options
	-------

	testscript:
		- do not include '.sikuli' extension

	testclass:
		- put the exact name of the class

	testrunnerType:
		- html
		- txt
		- defautl: txt

"""

import unittest

DEBUG = True


if __name__ == '__main__':

	args = sys.argv[1:]

	if DEBUG:
		print("Script: {}".format(getBundlePath()))
		print('Argument List: %s' % str(sys.argv))

	if len(args) >= 2:
		print("testscript: {}, testclass: {}".format(args[0], args[1]))
		module = __import__(args[0])
		my_class = getattr(module, args[1])
		test_suite = unittest.TestSuite()
		tests = unittest.TestLoader().loadTestsFromTestCase(my_class)
		test_suite.addTests(tests)
		if len(args) == 2:
			runner = unittest.TextTestRunner()
		elif len(args) == 3:
			print("arg for runner: {}".format(args[2]))
			if args[2] == "txt":
				runner = unittest.TextTestRunner()
			elif args[2] == "html":
				pass
		else:
			pass
		runner.run(test_suite)
	else:
		print("missing argument")
