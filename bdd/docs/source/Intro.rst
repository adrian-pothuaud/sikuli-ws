Intro - JePySi Test Automation Framework
========================================

JePySi Test Automation Framework is a collection of open source python scripts for the open source software sikuli, which can and should be used in conjunction with the open source CI server Jenkins. It uses a variation of the Gherkin DSL, used by Behave and Cucumber, to describe the test cases for a desktop or mobile app or a web site.

These test cases are put into feature files. The feature files have associated assets, constants, environments and python steps to interpret them within the JePySi scripts. The result is a test protocol, screenshots, a test log and junit test reports.

JePySi Test Automation Framework provides a faster, easier and comfortable repetitive way for developers and product owners to create desktop and mobile apps and web sites, which are automaticly tested. Over and over, again, may it be day or night.

- `MIT License`_ (year=2013,2014; copyright holders=arjs.net)
- Currently tested Browsers*: Chrome MAC; Chrome Windows; Chrome Linux
- Websites tested with JePySi: *arjs.net*, *jepysi.arjs.net*

Thanks for supporting our framework and enjoy!

Features
~~~~~~~~

1. Ready to launch!
^^^^^^^^^^^^^^^^^^^
You have everything built up, ready to launch your test suite with an easy setup for desktop based testing!

2. Use it anywhere!
^^^^^^^^^^^^^^^^^^^
JePySi is built not only to be used with browsers, but on smartphones and tablet apps, running in simulators, and desktop applications. It uses the ingenius sikuli.org tool, which was originaly developed by MIT, to visualy test for elements on the screen. If extended with Jenkins and virtual machines it can be used in a CI/CD scenario. E.g. arjs.net is an example for using a CI/CD process publishing a web site with JePySi Test Automation Framework.

3. Highly customizable!
^^^^^^^^^^^^^^^^^^^^^^^
You don't like the default values?, it's extremely easy to add or change elements, optimize the python code, add new features. Hey!, it's open source.

Prerequisits
~~~~~~~~~~~~

+ Skiuli IDE and Sikuli Script
+ Java
+ Text Editor or Python IDE, like Sublime Text or JetBrains PyCharme

Structure
~~~~~~~~~

* docs/ - Dokumentation; TBD
* examples/ - Some example features and step files;
* test/
	+ config/ - Configuration
  		+ config.txt - Global configurations
  		+ LINUX/
    		+ config.txt - Linux specific configuration
  		+ MAC/
    		+ config.txt - Mac specific configuration
  		+ WIN/
    		+ config.txt - Windows specific configuration
	+ features/ - Gherkin style feature files, ending with .feature
	+ images/ - PNG screenshots for sikuli; Should be taken with the Sikuli IDE
		+ linux - Linux specific images
		+ mac - Mac specific images
		+ win - Windows specific images
	+ runner.sikuli/ - JePySi core system scripts writen in Python; Subject to changes
	+ steps/ - The Python step files with the steps referenced in the feature files

Run tests
~~~~~~~~~

Start a jepysi test::

    <path to sikuli>runScript -r runner [-f <logfile for sikuli>] -- <environment> <feature or feature path>

- <path to sikuli>: The path to the sikuli script that starts the sikuli script system
- <logfile for sikuli>: Capturing the output from sikuli script
- '- -': Devides the sikuli arguments from the JePySi arguments
- <environment>: The specific environment to use by JePySi
- <feature or feature path>: Specify a single feature file or a folder with a bunch of feature files

`Important remark`: No wildcard support for feature files or folders

Help
~~~~
You want or need help or support for your initial setup. Contact me at info(at)arjs.net

Changelog
~~~~~~~~~
2014/02/20 Added Werk1 example

2014/02/09 Added documentation and a short tutorial; Some minor changes to the Readme files; Inline documentation fixes

2014/02/06 Redme Updates; First example

2014/02/01 Initial public release.

2013/12/01 Initial silent release.

Links
~~~~~
+ Jenkins CI Server - http://jenkins-ci.org
+ Python programming language - http://python.org
+ Sikuli Tool - http://sikuli.org
+ Behave Gherkin DSL Docs - http://docs.behat.org/guides/1.gherkin.html
+ JePySi pages - http://jepysi.arjs.net

JePySi Origins
~~~~~~~~~~~~~~
+ Ruby on Rail Style - Test Automation using Sikuli, Cucumber and Jenkins by Richard Foster `[1]`_
+ The Starting Point - Sikuli Test Framework by Josh McVey `[2]`_


Download the binary package
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://api.bintray.com/packages/alexrjs/generic/JePySi/images/download.png

`Download`_

.. _Download: http://dl.bintray.com/alexrjs/generic/JePySi/

Installation
~~~~~~~~~~~~
- Unjar the package to a place of your choice
- Copy the `test` folder to your project

.. _MIT License: http://opensource.org/licenses/mit-license.html

.. _[1]: http://prezi.com/arubpcolpmzv/?utm_campaign=share&utm_medium=copy&rc=ex0share

.. _[2]: http://www.youtube.com/watch?v=z_WTpH9XvYA
