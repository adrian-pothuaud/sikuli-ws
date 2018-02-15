# -*- coding:utf-8 -*-

'''This script is a module for scripts scaffolding for sikuli framework/scenarios'''

from sikuli import *

import os

def create_sikuli_script(path, content=None):
    '''create a complete sikuli script'''
    print('creation of a sikuli script at {}'.format(path))
    if not '.sikuli' in path:
        path.append('.sikuli')
    name = path.split('.')[-2].split(os.sep)[-1]
    os.system('mkdir {}'.format(path))
    os.system('touch {}{}{}.py'.format(path, os.sep, name))
    os.system('touch {}{}{}.html'.format(path, os.sep, name))
    if content:
        os.system('echo {} > {}{}{}.py'.format(content, path, os.sep, name))

if __name__ == '__main__':
    
    import path_utils
    create_sikuli_script(os.path.join(path_utils.get_parent_dirname(getBundlePath(), 2)), "specs", "AutoHello")
