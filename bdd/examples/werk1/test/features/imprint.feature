Environments:
	PROD	: url = http://www.werk1muenchen.de/

Assets:
	"Imprint title" = title-impressum.png
	"Address text" = text-impressum.png

Feature: Check if the imprint page is viewed correctly
	As a website owner I want to see a the imprint page,
	when I open the "imprint" link on the bottom of the page,
	so I can be sure I don't get sued.

Scenario: Check imprint elements
	Given I see the "#logo# logo" at the top
	And I see a "top menu"
	And I see a "social menu"
	And I should see the "imprint link" at the page end
	When I click the "imprint link"
	Then I should see the "#logo# logo" block
	And I should see the "Imprint title" block
	And I should see the "Address text" block
