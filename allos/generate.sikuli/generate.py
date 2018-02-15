# -*- coding:utf-8 -*-

'''This script is a module for scripts scaffolding for sikuli framework/scenarios'''

from sikuli import *

import os

DEFAULT_SCRIPT_BASE = [
    r"# -*- coding:utf-8 -*-",
    r"",
    r"'''DOCUMENT THIS MODULE HERE'''",
    r"",
    r"from sikuli import *",
    "",
    r"def default_fun():",
    "\t'''DOCUMENT THIS FUNCTION HERE'''",
    "\tprint('Hello Sikuli, I am scaffolded')",
    r"",
    r"default_fun()"
]

def create_sikuli_script(path, content=None):
    '''create a complete sikuli script'''
    print('creation of a sikuli script at {}'.format(path))
    if not '.sikuli' in path:
        path = u'{}.sikuli'.format(path)
    name = path.split('.')[-2].split(os.sep)[-1]
    os.system('mkdir {}'.format(path))
    os.system('touch {}{}{}.py'.format(path, os.sep, name))
    os.system('touch {}{}{}.html'.format(path, os.sep, name))
    if content:
        with open('{}{}{}.py'.format(path, os.sep, name), 'w') as fout:
            for l in content:
                fout.write("{}\n".format(l))

if __name__ == '__main__':

    import sys

    if not '.sikuli' in sys.argv[-1]:
        create_sikuli_script(sys.argv[-1], DEFAULT_SCRIPT_BASE)
    else:
        raise ValueError("missing argument for module name, usage: 'java -jar sikulix.jar -r generate.sikuli --args module_name'")
