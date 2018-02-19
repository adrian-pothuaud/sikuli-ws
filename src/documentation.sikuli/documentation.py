# -*- coding:utf-8 -*-

"""

"""

import pydoc

import sikuli
import applications

python_imports = [ "glob", "pydoc" ]
other_imports = [ "path_utils", "image_utils" ]
sikuli_elems = [ i for i in dir(sikuli) ]

elems = [ i for i in dir(applications)
    if not i in sikuli_elems
    and not i in other_imports
    and not i in python_imports ]

for elem in elems:
    try:
        elem_help = pydoc.render_doc(elem, "Help on {}".format(elem))
        print(elem_help)
    except:
        pass
