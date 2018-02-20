Environments:
	PROD	: url = http://www.werk1muenchen.de/

Feature: Check the extra features on the #domain# page
	As a website owner I want to check the extra features on the #domain# page,
	when I enter the domain "#domain#" url in the browser url field,
	so I'm sure the end user has the complete experience.

Scenario: Check #domain# logo link
	Given I see the "#logo# logo"
	When I click the "#logo# logo"
	Then I should see the "#logo# logo" after 1s

Scenario: Check footer block
	Given I see the "#logo# logo"
	Then I should see "footer" block at the page end

Scenario: Check Facebook like
	Given I see the "#logo# logo"
	And I see a "facebook like" logo at the page end
	Then I should be able to hover over the "facebook like" logo

Scenario: Check Hotspot link
	Given I see the "#logo# logo"
	And I see a "hotspot link"
	Then I should be able to hover over the "hotspot link"

Scenario: Check imprint link
	Given I see the "#logo# logo"
	And I see the "bottom menu" block at the page end
	When I click the "imprint link"
	Then I should see the "imprint title" block after 1s

Scenario: Check Social block
	Given I see the "#logo# logo"
	And I see the "social menu" block
	Then I should be able to hover over the "rss logo" link
	And I should be able to hover over the "twitter logo" link
	And I should be able to hover over the "facebook logo" link

Scenario: Check Bottom menu
	Given I see the "#logo# logo"
	And I see the "bottom menu" block at the page end
	Then I should be able to hover over the "imprint link"
	And I should be able to hover over the "press link"
	And I should be able to hover over the "events link"
	And I should be able to hover over the "mieterinfos link"
	And I should be able to hover over the "mieterwerden link"
	And I should be able to hover over the "anfahrt link"
