based on [tutorial](http://supersabrams.com/blog/?p=386)

Requirements
============

Create Jython virtualenv
------------------------

- You should have Python AND Jython already installed
- Install PIP (Python Package Manager) from [pip.pypa.io](https://pip.pypa.io/en/stable/installing/)
- type in CLI

      pip install virtualenv
      cd your_project_path
      virtualenv -p jython jyvenv

Configure virtual environment
-----------------------------


- You should add sikulix.jar to Java classpath
  - Windows:

    right click hard drive -> properties -> advanced system settings -> environment variables -> modify or create CLASSPATH

  - Mac:

    edit ./bash_profile and add

        export CLASPPATH=path_to_sikulix.jar

  - Linux:

    ...

- You should add sikulix.jar/Lib/sikuli to jyvenv/Lib
  - Windows:

    use archive tool like 7zip -> view archive -> go to Lib/ -> right click sikuli folder -> copy to

  - Mac:
    - extract sikulix.jar

          tar xf sikulix.jar

    - copy sikuli library to virtual environment

          sudo cp -R /Applications/SikuliX.app/Contents/Java/Lib/sikuli path_to_jyvenv/Lib/

    - grant execution rights on jython/pip

          sudo chmod +x jyvenv/bin/jython
          sudo chmod +x jyvenv/bin/pip

  - Linux:

    ...


Install additional dependencies
-------------------------------
