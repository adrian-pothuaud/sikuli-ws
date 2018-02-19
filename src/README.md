Sources Folder
==============

**Sources modules are intended for delivering sikuli advanced features and custom functions.**

Write new sources
-----------------

##### *Follow below instructions*

### Script template

**Use this template and write your code.**

    # -*- coding:utf-8 -*-

    """
    description: ...
    status: ...
    .. todo:: ...
    .. sectionauthor:: ...
    """

    from sikuli import *		    # import sikuli features

    import specscontext			 # context -> add additional sources in path

    import path_utils, generate     # example import from src
    import Browser, Chrome          # example import from objects

    # DO YOUR STUFF below

    # just an example
    c1 = new Chrome()
    c1.open()
    c1.new_tab("https://github.com/adrianpothuaud/sikuli-ws")


**Comment your code !**

**Use specscontext with a simple line:**

    import specscontext

=> this enables imports for modules in src/ and src/objects/ !

:sunglasses:
