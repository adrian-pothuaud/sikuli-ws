# -*- coding:utf-8 -*-

"""
    The ``generate`` module
    ======================

    Use it to import sikuli specific scaffolding functions.

    Module content
    --------------

    - DEFAULT_SCRIPT_BASE
    - create_sikuli_script

    Module state
    ------------
    status: OK (02-19-2018)
    test: run specs/scripts_scaffolding.sikuli

    ..todo:: Sort functions in alphabetical order
    .. sectionauthor:: Adrian Pothuaud <adrianpothuaud2@gmail.com>

"""

from sikuli import *

import os

DEBUG = True

DEFAULT_SCRIPT_BASE = [
    r"# -*- coding:utf-8 -*-",
    r"",
    r'"""',
    r'DOCUMENT THIS MODULE HERE',
    r'"""',
    r"",
    r"from sikuli import *",
    "",
    r"import specscontext",
    "",
    r"def default_fun():",
    "\t\"\"\"",
    "\tDOCUMENT THIS FUNCTION HERE",
    "\t\"\"\"",
    "\tprint('Hello Sikuli, I am scaffolded')",
    r"",
    r"default_fun()"
]

def create_sikuli_script(path, content=DEFAULT_SCRIPT_BASE):
    """
    Create a complete sikuli module

    Create a Sikuli module following this architecture:
    name.sikuli
    |__ name.py
    |__ name.html

    :param path: Path for the new .sikuli folder.
    :param content: .py file content (default is DEFAULT_SCRIPT_BASE).
    :type path: A string representing a path. Ends with '.sikuli'.
    :type content: A list of strings representing lines in future file.
    :return: {"sikuli": path, "python": pyfile, "html": htmlfile}
    :rtype: dic

    """
    # ToDo: add parameter for script to be specs/src/object
    # ToDo: change DEFAULT_SCRIPT_BASE to DEFAULT_SPEC_CONTENT
    if DEBUG:
        print('creation of a sikuli script: {}'.format(path))
    if not '.sikuli' in path:
        path = u'{}.sikuli'.format(path)
    name = path.split('.')[-2].split(os.sep)[-1]
    try:
        os.mkdir(path)
        if DEBUG:
            print("{} folder created".format(path))
    except OSError:
        if DEBUG:
            print("{} folder already exists".format(path))
    htmlfile = os.path.join(path, "{}.html".format(name))
    with open(htmlfile, 'w') as f:
        f.write('')
    if DEBUG:
        print("{} file created".format(htmlfile))
    pyfile = os.path.join(path, "{}.py".format(name))
    with open(pyfile, 'w') as f:
        for l in content:
            f.write("{}\n".format(l))
    if DEBUG:
        print("{} file created".format(pyfile))
    return {"sikuli": path, "python": pyfile, "html": htmlfile}
