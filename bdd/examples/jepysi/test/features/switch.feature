Assets:
	"buttons sidebar" = block-sidebar.png
	"<button> dot" = block-sidebar.png
	"<title> dot" = dot-<selected>.png
	"<title> title" = title-<selected>.png

Environments:
	LOCAL	: url = localhost:8090/index.html
	DEV		: url = dev.jepysi.arjs.net/index.html
	STAGE	: url = stage.jepysi.arjs.net/index.html
	PROD	: url = jepysi.arjs.net/index.html

Feature: Check and Click the pages of the #domain# website
	As a website owner I want to be sure that,
	when I click the pages buttons of the "#domain#" website,
	I see the associated page of each button.

Scenario Outline: Hover and Click Page Buttons
	Given I see the "buttons sidebar"
	And I see the "JePySi title"
	When I hover over the "<button> dot"
	And I click the "<button> dot"
	Then I should see the "<title> title after 1s"
	And I should see the "<title> dot"

Examples: Pages Full
	| button	| title		| selected	| dx	| dy 	|
	| First		| JePySi 	| jepysi	| 0		| -60	|
	| Second	| Jenkins	| jenkins	| 0		| -38 	|
	| Third		| Python 	| python	| 0		| -15 	|
	| Fourth	| Sikuli	| sikuli	| 0		| 15 	|
	| Fifth		| Gherkin	| gherkin	| 0		| 34 	|
	| Sixth		| Thank You	| thankyou	| 0		| 60 	|
