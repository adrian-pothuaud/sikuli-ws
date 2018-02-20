Environments:
	LOCAL	: url = localhost:8090/imprint.html
	DEV		: url = dev.jepysi.arjs.net/imprint.html
	STAGE	: url = stage.jepysi.arjs.net/imprint.html
	PROD	: url = jepysi.arjs.net/imprint.html

Assets:
	"Address" = block-address.png
	"UstId" = block-ustid.png
	"Release date" = block-release-date.png
	"black Tested with" = block-tested-imprint.png

Feature: Check if the imprint page is viewed correctly
	As a website owner I want to see a the imprint page,
	when I open the "imprint" link on the top of the page,
	so I can be sure I don't get sued.

Scenario: Check imprint elements
	Given I see the "JePySi title link"
	And I see a "arjs.net link"
	And I see a "imprint link"
	Then I should see the "imprint" title
	And I should see the "Address" block
	And I should see the "UstId" block
	And I should see the "Release date" block at the page end
	And I should see a "black Tested with" message
