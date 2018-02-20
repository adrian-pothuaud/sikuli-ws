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