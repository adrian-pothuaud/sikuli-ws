
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

Identify Repeated code
----------------------

		import webbrowser               # python web browser automation


		# open google
		webbrowser.open("http://www.google.com")
		wait("google.png")             # repeated "google.png"
		# type 'Sikuli'
		click("google.png")            # repeated "google.png"
		paste("Sikuli")
		wait(0.5)
		# search
		Region(200, 200, 200, 200).getCenter().click()
		wait(1)
		click("search.png")
		# wait result
		wait("sikuli-script-home.png")

The Final script
----------------


Run the script
--------------

in a shell write

	java -jar path_to_sikulix.jar -r path_to_script.sikuli


___


[Previous Tuto]() <-----------------------------> [Next Tuto]()

___


last update 2/19/2018

:sunglasses:
