#!/usr/bin/env jython
import sys
from cucumber.cli import Main

Main.run(sys.argv[1:], Main.getClassLoader())
