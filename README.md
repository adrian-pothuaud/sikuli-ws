Sikuli Workspace for GUI automation
===================================

This is an example on how to use Sikuli with python for GUI testing.

What is [SikuliX](http://sikulix.com/) ?
----------------

> Automate what you see on a computer monitor
>
> SikuliX automates anything you see on the screen of your desktop computer running Windows, Mac or some Linux/Unix. It uses image recognition powered by OpenCV to identify and control GUI components. This is handy in cases when there is no easy access to a GUI's internals or the source code of the application or web page you want to act on.

> Besides locating images on a screen SikuliX can run the mouse and the keyboard to interact with the identified GUI elements. This is available for multi monitor environments and even for remote systems with some restrictions.

>SikuliX comes with basic text recognition (OCR) and can be used to search text in images. This feature is powered by Tesseract.



How to use [SikuliX](http://sikulix.com/) ?
-------------------

> SikuliX supports as scripting languages
Python language level 2.7 (supported by Jython)
running RobotFramework text-scripts is supported (see docs)
Ruby language level 1.9 and 2.0 (supported by JRuby)
JavaScript (supported by the Java Scripting Engine)
… and you can use it in Java programming and programming/scripting with any Java aware programming/scripting language (Jython, JRuby, Scala, Clojure, …).

> Though SikuliX is currently not available on any mobile device, it can be used with the respective emulators on a desktop computer or based on VNC solutions. A solution for Android devices based on ADB (Android Debugging Bridge) is in an early experimental stage,

How to better use [SikuliX](http://sikulix.com/) ?
-------------------

- Define a clean workspace
- Add Best Practices
- Make your own experience
- Collaborate
- Use TDD/BDD
- Share results
- more ...

**Proposed** workspace structure
-------------------

#### [bdd](https://github.com/adrianpothuaud/sikuli-ws/tree/master/bdd)

Some tests to integrate BDD language with Sikuli testing ...

Not achieved yet ... :cold_sweat:


#### [imgs](https://github.com/adrianpothuaud/sikuli-ws/tree/master/imgs)

An Image Library to put all script images in one place.

Pros | Cons
---- | ----
All images in the same place | No more images in scripts using Sikuli IDE
Do not repeat images (DRY)   | Harder to do offsets


#### [jython](https://github.com/adrianpothuaud/sikuli-ws/tree/master/jython)


A proposed workspace to use Sikuli features directly into python files and modules.

To be used as an external project.

You can either choose to continue with jython or remove it from SikuliX-style workspace.

Pros | Cons
---- | ----
no .sikuli parent | interprete with Jython
easier imports   | no more available in SikuliX IDE
additional dependencies available with pip  |
support for virtual environments  |


#### [out](https://github.com/adrianpothuaud/sikuli-ws/tree/master/out)

Outputs Folder containing any output from the scripts.

e.g: test reports.

#### [specs](https://github.com/adrianpothuaud/sikuli-ws/tree/master/specs)

On-the-go testing and demonstrations.

#### [src](https://github.com/adrianpothuaud/sikuli-ws/tree/master/src)

Improved and custom sikuli features for image recognition and GUI interactions.

#### [tests](https://github.com/adrianpothuaud/sikuli-ws/tree/master/tests)

- Unit tests for every sources.
- Test scenarios for applications(GUI testing).

#### [tutos](https://github.com/adrianpothuaud/sikuli-ws/tree/master/tutos)

A tutorials series for Sikuli and how to create a workspace similar to this one.
On coming: tutorial to test the GUI of an application the proper way and validate or not distribution.


Supported environments
----------------------

**Windows**

**OsX**

**Linux**
