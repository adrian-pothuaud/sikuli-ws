Tutorial
========

Step 1
~~~~~~
Setup your test environment.

- Create your project folder
- Unpack jepysi.jar
- Copy the `test` folder to your project folder

Step 2
~~~~~~
Write your first feature into a feature file e.g. `first.feature`

.. code-block:: text

	Feature: Check the JePySi basics
		 As a End-User I want to see the basic elements of the #domain#,
		 when I enter the [url] in a new tab,
		 so I'm sure that the website is complete.

	Scenario: Check the basics
		  Given I have an open a browser
		  When I enter the [url] in a new tab
		  Then I should see the "JePySi doc link"
		  And I should see the "JePySi Welcome" title
		  And I should see the "Top Navigation" on the left top
		  And I should see the "Navigation" on the left

Some remarks:

- #domain# is a constant
- [url] is an environment specific variable
- Text in double quotes are assets

Step 3
~~~~~~
Run your first test::

    <path to sikuli>runScript -r runner -f log.txt -- LOCAL features/first.feature

Some remarks:

- <path to sikuli>: Path to the sikuli script
- "-f log.txt": Capture all sikuli outputs to a file "log.txt"
- "LOCAL": Use the local environment settings
- "features/first.feature" use this feature file

Output::

	filename 'README.md' ignored...
	Import Took: 0:00:00.001000
	WARNING: given step not found: I have an open a browser
	WARNING: when step not found: I enter the [url] in a new tab
	WARNING: then step not found: I should see the "JePySi doc link"
	WARNING: then step not found: I should see the "JePySi Welcome" title
	WARNING: then step not found: I should see the "Top Navigation" on the left top
	WARNING: then step not found: I should see the "Navigation" on the left
	===========================================================================
	# File: /Users/alexrjs/Work/Code/py/jepysi/test/features/first.feature
	---------------------------------------------------------------------------
	ERROR: Exception (processfeature): Undefined steps. Cannot continue!
	FAILED: Feature Took: 0:00:00.012001
	Features Took: 0:00:00.022000

	0 loaded steps, 0 processed, 0 passed, 0 failed, 0 skipped, 6 undefined
	1 loaded scenarios, 0 processed, 0 passed, 0 failed, 0 skipped
	1 loaded features, 1 processed, 0 passed, 1 failed
	0 loaded assets, 0 unknown
	---------------------------------------------------------------------------
	@then(u'I should see the "Navigation" on the left')
	def step_impl(testcontext):
		asset = testcontext.assets["Navigation"]
		assert testcontext.browser.failed(testcontext.info, asset), testcontext.info


	@then(u'I should see the "JePySi Welcome" title')
	def step_impl(testcontext):
		asset = testcontext.assets["JePySi Welcome"]
		assert testcontext.browser.failed(testcontext.info, asset), testcontext.info


	@then(u'I should see the "JePySi doc link"')
	def step_impl(testcontext):
		asset = testcontext.assets["JePySi doc link"]
		assert testcontext.browser.failed(testcontext.info, asset), testcontext.info


	@given(u'I have an open a browser')
	def step_impl(testcontext):
		assert testcontext.browser.failed(testcontext.info, asset), testcontext.info


	@then(u'I should see the "Top Navigation" on the left top')
	def step_impl(testcontext):
		asset = testcontext.assets["Top Navigation"]
		assert testcontext.browser.failed(testcontext.info, asset), testcontext.info


	@when(u'I enter the [url] in a new tab')
	def step_impl(testcontext):
		assert testcontext.browser.failed(testcontext.info, asset), testcontext.info


**Problem:** Steps are not defined.

Step 4
~~~~~~
Fix the step problems:

- Mark the steps on the console copy them
- Open a new step file, e.g. `step.py` in the `steps` folder
- Put the following lines into the step file::

	from sikuli.Sikuli import *
	from case import *

- Paste the copied steps into the step file
- Edit the "I have an open a browser" and the "I enter the [url] in a new tab" assert and replace ", asset with "''" (two single quotes), to prevent an "asset" not defined error.
- Do a second run

Output::

	filename 'README.md' ignored...
	Importing step file step.py
	Import Took: 0:00:00.013000
	===========================================================================
	# File: /Users/alexrjs/Work/Code/py/jepysi/test/features/first.feature
	---------------------------------------------------------------------------
	ERROR: Asset definition 'JePySi doc link' not found!
	ERROR: Asset definition 'JePySi Welcome' not found!
	ERROR: Asset definition 'Top Navigation' not found!
	ERROR: Asset definition 'Navigation' not found!
	ERROR: Exception (assetsdefinedcheck): Missing assets. Cannot continue!
	FAILED: Feature Took: 0:00:00.014000
	Features Took: 0:00:00.031000

	6 loaded steps, 0 processed, 0 passed, 0 failed, 0 skipped, 0 undefined
	1 loaded scenarios, 0 processed, 0 passed, 0 failed, 0 skipped
	1 loaded features, 1 processed, 0 passed, 1 failed
	0 loaded assets, 4 unknown
	---------------------------------------------------------------------------
	"Top Navigation" = ?
	"Navigation" = ?
	"JePySi doc link" = ?
	"JePySi Welcome" = ?
	===========================================================================

**Problem:** Assets are not defined. You can use the assets list at the bottom as template

Step 5
~~~~~~
Fix the assets problems:

- Start the Sikuli IDE and take screenshots from you assets and give them a good name
- Save the Sikuli IDE project to good place with a good name, e.g. "first" - the actual name would be "first.sikuli"
- Copy the images from the "first.sikuli" folder to the `images` folder within the `test` folder
- Add the Assets section to the feature file::

	Assets:
		"Top Navigation" = block-top-navi.png
		"Navigation" = block-navi.png
		"JePySi doc link" = link-jepysi-doc.png
		"JePySi Welcome" = title-jepysi-welcome.png

- Do a third run

Output::

	filename 'README.md' ignored...
	Importing step file step.py
	Import Took: 0:00:00.011000
	===========================================================================
	# File: /Users/alexrjs/Work/Code/py/jepysi/test/features/first.feature
	---------------------------------------------------------------------------
	Feature: Check the JePySi basics
	ERROR: Exception (Feature): domain
	---------------------------------------------------------------------------
	ERROR: Exception (processfeature): domain
	FAILED: Feature Took: 0:00:00.026000
	Features Took: 0:00:00.047001

	6 loaded steps, 0 processed, 0 passed, 0 failed, 0 skipped, 0 undefined
	1 loaded scenarios, 0 processed, 0 passed, 0 failed, 0 skipped
	1 loaded features, 1 processed, 0 passed, 1 failed
	4 loaded assets, 0 unknown
	===========================================================================

**Problem:** Constants are not defined.

Step 6
~~~~~~
Fix the constants problems:

- Add the Constant section to the feature file::

	Constants:
		domain = jepysi.arjs.net/docs/

- Do a fourth run

Output::

	filename 'README.md' ignored...
	Importing step file step.py
	Import Took: 0:00:00.013001
	===========================================================================
	# File: /Users/alexrjs/Work/Code/py/jepysi/test/features/first.feature
	---------------------------------------------------------------------------
	Feature: Check the JePySi basics
	         As a End-User I want to see the basic elements of the jepysi.arjs.net/docs/,
	         when I enter the [url] in a new tab,
	         so I'm sure that the website is complete.
	---------------------------------------------------------------------------
	  Check the basics
	    FAILED: Given: I have an open a browser ... failed in 0:00:00.588000
	    Scenario Took: 0:00:00.591000

	FAILED: Feature Took: 0:00:00.620001
	Features Took: 0:00:00.630999

	6 loaded steps, 1 processed, 0 passed, 1 failed, 0 skipped, 0 undefined
	1 loaded scenarios, 1 processed, 0 passed, 1 failed, 0 skipped
	1 loaded features, 1 processed, 0 passed, 1 failed
	4 loaded assets, 0 unknown
	===========================================================================

**Problem:** The **first** failed test.

Step 7
~~~~~~
Fix the run problems:

- Open the steps file and fix the failed test::

	@given(u'I have an open a browser')
	def step_impl(testcontext):
		assert testcontext.browser.open(), testcontext.info

- Do another run

Output::

	filename 'README.md' ignored...
	Importing step file step.py
	Import Took: 0:00:00.009000
	===========================================================================
	# File: /Users/alexrjs/Work/Code/py/jepysi/test/features/first.feature
	---------------------------------------------------------------------------
	Feature: Check the JePySi basics
	         As a End-User I want to see the basic elements of the jepysi.arjs.net/docs/,
	         when I enter the [url] in a new tab,
	         so I'm sure that the website is complete.
	---------------------------------------------------------------------------
	  Check the basics
	    PASSED: Given: I have an open a browser ... passed in 0:00:02.777000
	    ERROR: Exception: When: I enter the [url] in a new tab - LOCAL
	    Scenario Took: 0:00:02.784001

	FAILED: Feature Took: 0:00:02.815000
	Features Took: 0:00:02.823999

	6 loaded steps, 2 processed, 1 passed, 1 failed, 0 skipped, 0 undefined
	1 loaded scenarios, 1 processed, 0 passed, 1 failed, 0 skipped
	1 loaded features, 1 processed, 0 passed, 1 failed
	4 loaded assets, 0 unknown
	===========================================================================

**Problem:** The environment "LOCAL" is not defined.

Step 8
~~~~~~
Fix the environment problems:

- Add the Environment section to the feature file::

	Environments:
		LOCAL	: url = localhost:8090/docs/index.html
		PROD	: url = jepysi.arjs.net/docs/index.html

- The final feature file should look like this now:

	.. code-block:: text

		Assets:
			"Top Navigation" = block-top-navi.png
			"Navigation" = block-navi.png
			"JePySi doc link" = link-jepysi-doc.png
			"JePySi Welcome" = title-jepysi-welcome.png

		Constants:
			domain = jepysi.arjs.net/docs/

		Environments:
			LOCAL	: url = localhost:8090/docs/index.html
			PROD	: url = jepysi.arjs.net/docs/index.html

		Feature: Check the JePySi basics
				 As a End-User I want to see the basic elements of the #domain#,
				 when I enter the [url],
				 so I'm sure that the website is complete.

		Scenario: Check the basics
				  Given I have an open a browser
				  When I enter the [url] in a new tab
				  Then I should see the "JePySi doc link"
				  And I should see the "JePySi Welcome" title
				  And I should see the "Top Navigation" on the left top
				  And I should see the "Navigation" on the left


- Do another run

Output::

	filename 'README.md' ignored...
	Importing step file step.py
	Import Took: 0:00:00.016999
	===========================================================================
	# File: /Users/alexrjs/Work/Code/py/jepysi/test/features/first.feature
	---------------------------------------------------------------------------
	Feature: Check the JePySi basics
	         As a End-User I want to see the basic elements of the jepysi.arjs.net/docs/,
	         when I enter the localhost:8090/docs/index.html in a new tab,
	         so I'm sure that the website is complete.
	---------------------------------------------------------------------------
	  Check the basics
	    PASSED: Given: I have an open a browser ... passed in 0:00:02.701000
	    FAILED: When: I enter the localhost:8090/docs/index.html ... failed in 0:00:00.282000
	    Scenario Took: 0:00:02.997999

	FAILED: Feature Took: 0:00:03.038000
	Features Took: 0:00:03.050000

	6 loaded steps, 2 processed, 1 passed, 1 failed, 0 skipped, 0 undefined
	1 loaded scenarios, 1 processed, 0 passed, 1 failed, 0 skipped
	1 loaded features, 1 processed, 0 passed, 1 failed
	4 loaded assets, 0 unknown
	===========================================================================

**Problem:** Step failed. Ok, lets fix it. And while we on it, we implement the rest, too.

Step 9
~~~~~~
Fix the run problems:

- Open the steps file and fix the failed test::

	@when(u'I enter the [url] in a new tab')
	def step_impl(testcontext):
	    assert testcontext.browser.failed(testcontext.info, ''), testcontext.info

	with:

	@when(u'I enter the [url] in a new tab')
	def step_impl(testcontext):
	    assert testcontext.browser.opentab(), testcontext.info
	    envurl = testcontext.environments[testcontext.environment]["url"]
	    assert testcontext.browser.navigateto(envurl), testcontext.info

- While we on it we fix the rest, so the step file looks like this:

	.. code-block:: python

		from sikuli.Sikuli import *
		from case import *

		@then(u'I should see the "Navigation" on the left')
		def step_impl(testcontext):
		    asset = testcontext.assets["Navigation"]
		    assert testcontext.browser.checkifexists(asset), testcontext.info


		@then(u'I should see the "JePySi Welcome" title')
		def step_impl(testcontext):
		    asset = testcontext.assets["JePySi Welcome"]
		    assert testcontext.browser.checkifexists(asset), testcontext.info


		@then(u'I should see the "JePySi doc link"')
		def step_impl(testcontext):
		    asset = testcontext.assets["JePySi doc link"]
		    assert testcontext.browser.checkifexists(asset), testcontext.info


		@given(u'I have an open a browser')
		def step_impl(testcontext):
		    assert testcontext.browser.open(), testcontext.info


		@then(u'I should see the "Top Navigation" on the left top')
		def step_impl(testcontext):
		    asset = testcontext.assets["Top Navigation"]
		    assert testcontext.browser.checkifexists(asset), testcontext.info


		@when(u'I enter the [url] in a new tab')
		def step_impl(testcontext):
		    assert testcontext.browser.opentab(), testcontext.info
		    envurl = testcontext.environments[testcontext.environment]["url"]
		    assert testcontext.browser.navigateto(envurl), testcontext.info
		    assert testcontext.browser.enterkey(Key.ENTER), testcontext.info

- Do another run

Output::

	filename 'README.md' ignored...
	Importing step file step.py
	Import Took: 0:00:00.011999
	===========================================================================
	# File: /Users/alexrjs/Work/Code/py/jepysi/test/features/first.feature
	---------------------------------------------------------------------------
	Feature: Check the JePySi basics
	         As a End-User I want to see the basic elements of the jepysi.arjs.net/docs/,
	         when I enter the localhost:8090/docs/index.html,
	         so I'm sure that the website is complete.
	---------------------------------------------------------------------------
	  Check the basics
	    PASSED: Given: I have an open a browser ... passed in 0:00:02.728001
	    PASSED: When: I enter the localhost:8090/docs/index.html in a new tab ... passed in 0:00:02.808001
	    PASSED: Then: I should see the "JePySi doc link" ... passed in 0:00:06.715001
	    PASSED: Then: I should see the "JePySi Welcome" title ... passed in 0:00:01.441000
	    PASSED: Then: I should see the "Top Navigation" on the left top ... passed in 0:00:01.542001
	    PASSED: Then: I should see the "Navigation" on the left ... passed in 0:00:01.434000
	    Scenario Took: 0:00:16.680001

	PASSED: Feature Took: 0:00:16.714000
	Features Took: 0:00:16.723999

	6 loaded steps, 6 processed, 6 passed, 0 failed, 0 skipped, 0 undefined
	1 loaded scenarios, 1 processed, 1 passed, 0 failed, 0 skipped
	1 loaded features, 1 processed, 1 passed, 0 failed
	4 loaded assets, 0 unknown
	===========================================================================

**Congrats:** You've successfully created and run your first "JePySi" test.

Step 10
~~~~~~~
Some remarks:

- Of course you can combine the steps. In fact when you get more experience, you certainly will do steps right away to avoid unneccessary runs

- If you do more feature files, you'll see there is a lot of dublication involved, so you should start using the simple inheritance system. E.g. put stuff into "_" feature files and use special scenarios like "Setup", "Cleanup", "After" and "Before". See the "JePySi" sample to see these features in action and how to use them

- Group feature files which belong together into folders

- In case you encounter different rendering, use the "OR" feature in the Assets definition; See "JePySi" example for the usage

- Start using Jenkins as CI System and use JePySi within Jenkins together with VMs, if you can

- Check out the "logs" and "reports" folder for their information, to see how you can use them

- If you have questions or feedback, get in touch with me at info(at)arjs.net



Have fun...