Environments:
	LOCAL	: url = localhost:8090/index.html
	DEV		: url = dev.jepysi.arjs.net/index.html
	STAGE	: url = stage.jepysi.arjs.net/index.html
	PROD	: url = jepysi.arjs.net/index.html

Feature: Check the basics of the #domain# #page# page
	As a website owner I want to see a complete #page# page on the website,
	when I enter the domain "#domain#",
	so I'm sure I have the complete experience

Scenario: Check #page# Page
	Given I see the "JePySi title link"
	And I see the "first page" selected
	When I press the DOWN key #count# times
	Then I should see the "#page# title"
	And I should see a "#page# text" message
	And I should see a "arjs.net link"
	And I should see the "JePySi title link"
	And I should see a "imprint link"
	And I should see a "Bitbucket link"
	And I should see a "Tested with" message
	And I should see a "Bintray link"
