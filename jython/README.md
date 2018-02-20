Requirements
============

Create Jython virtualenv
------------------------

- You should have Python AND Jython already installed
- Install PIP (Python Package Manager) from [pip.pypa.io](https://pip.pypa.io/en/stable/installing/)

  or type (Linux):

    sudo apt install python-pip

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

    export CLASSPATH="/home/adrian/sikuli/sikulix.jar"


- You should add sikulix.jar/Lib/sikuli to jyvenv/Lib
  - Windows:

    use archive tool like 7zip -> view archive -> go to Lib/ -> right click sikuli folder -> copy to

  - Mac:
    - extract sikulix.jar

          jar xf sikulix.jar

    - copy sikuli library to virtual environment

          sudo cp -R /Applications/SikuliX.app/Contents/Java/Lib/sikuli path_to_jyvenv/Lib/

    - grant execution rights on jython/pip

          sudo chmod +x jyvenv/bin/jython
          sudo chmod +x jyvenv/bin/pip

  - Linux:

    - extract sikulix.jar

          jar xf sikulix.jar

    - copy sikuli library to virtual environment

          sudo cp -R sikuli/Lib/sikuli path_to_jyvenv/Lib/

    - grant execution rights on jython/pip

          sudo chmod +x jyvenv/bin/jython
          sudo chmod +x jyvenv/bin/pip

- Also add sikulix.jar to jyvenv/javalib


Install additional dependencies
-------------------------------

    jyvenv/bin/pip install xxxxxxxxxx
    jyvenv/bin/pip install -r requirements.txt

Run a script
------------

    jyvenv/bin/jython tests/sample_test.py
