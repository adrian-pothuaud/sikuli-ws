
Sikuli Tutorial n°2
===================

*Use variables*
------------------------------------

Scenario: Search 'Sikuli' in Google
-------------------------

1. open web browser
2. go to 'http://www.google.com'
3. type 'Sikuli' in search bar
4. click search button
5. wait for first result (should be SikuliX website)

DRY Principle
-------------

DONT REPEAT YOURSELF !

Variables are a first step to DRY principle that is very important in programming.
In one hand it makes code cleaner and more compact, in another it allows faster developement.

For this tutorial we'll copy the previous one "simple script" and rearrange the code.

But first let use the Sikuli interpreter to test variables "on-the-go".

Using Variables
---------------

In your command line interface run:

		path_to_sikuli/runsikulix -i

or run it directly if it has been added to your PATH...

This will launch Sikuli interactive session.

		$ runsikulix -i
		+++ running this Java
		java version "1.8.0_121"
		Java(TM) SE Runtime Environment (build 1.8.0_121-b13)
		Java HotSpot(TM) 64-Bit Server VM (build 25.121-b13, mixed mode)
		+++ trying to run SikuliX
		+++ using: -Xms64M -Xmx512M -Dfile.encoding=UTF-8 -Dsikuli.FromCommandLine -jar C:\SikuliX\sikulix.jar -i
		Hello, this is your interactive Sikuli (rules for interactive Python apply)
		use the UP/DOWN arrow keys to walk through the input history
		help()<enter> will output some basic Python information
		... use ctrl-d to end the session
		>>>

Then type:

		a = capture()

This will let you take a screenshot... You can then play wit your new variable 'a'

		>>> a = capture()
		>>> a
		u'C:\\Users\\apd2\\AppData\\Local\\Temp\\Sikulix_1050016890\\sikuliximage-1519141728792.png'
		>>> wait(a)
		M[271,1043 39x31]@S(S(0)[0,0 1920x1080]) S:1.00 C:290,1058 [491 msec]
		>>> hover(a)
		1
		>>> click(a)
		[log] CLICK on L(290,1058)@S(0)[0,0 1920x1080] (521 msec)
		1

Identify potential variables
----------------------------

Anything that:
- is repeated
- is potentialy changeable

Should become a variable.

		import webbrowser              				# python web browser automation


		# open google
		webbrowser.open("http://www.google.com") 	  # can change
		wait("google.png")                             # repeated "google.png"
		# type 'Sikuli'
		click("google.png")            			    # repeated "google.png"
		paste("Sikuli")								# can change
		wait(0.5)					  				# can change
		# search
		Region(200, 200, 200, 200).getCenter().click() # region can change
		wait(1)										# can change
		click("search.png")						    # can change
		# wait result
		wait("sikuli-script-home.png") 				# can change


Modify the script
-----------------

		import webbrowser               # python web browser automation


		# reusable variables
		url         = "http://www.google.com"
		google      = "google.png"
		query       = "SikuliX"
		topleft     = Region(200, 200, 200, 200)
		search      = "search.png"
		defaultWait = 0.5
		result      = "sikuli-script-home.png"


		# open an url
		webbrowser.open(url)
		wait(google)

		# type a query
		click(google)
		paste(query)
		wait(defaultWait)

		# search
		topleft.getCenter().click()
		wait(defaultWait)
		click(search)

		# wait result
		wait(result)


Run the script
--------------

in a shell write

	java -jar path_to_sikulix.jar -r path_to_script.sikuli


___


[Previous Tuto]() <-----------------------------> [Next Tuto]()

___


last update 2/19/2018

:sunglasses:
