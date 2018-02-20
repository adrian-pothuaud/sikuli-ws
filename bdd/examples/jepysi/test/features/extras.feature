Environments:
	LOCAL	: url = localhost:8090/index.html
	DEV		: url = dev.jepysi.arjs.net/index.html
	STAGE	: url = stage.jepysi.arjs.net/index.html
	PROD	: url = jepysi.arjs.net/index.html

Feature: Check the extra features on a page
	As a website owner I want to check the extra features on a page,
	when I enter the domain "#domain#",
	so I'm sure I have the complete experience

Scenario: Check arjs.net link
	Given I see the "JePySi title link"
	And I see a "arjs.net link"
	When I click the "arjs.net link"
	Then I should see the "arjs.net company logo" after 5s
	Then I should be able to close the "arjs.net company logo" tab after 5s

Scenario: Check Home link
	Given I see the "JePySi title link"
	When I click the "JePySi title link"
	Then I should see the "JePySi title" after 1s

Scenario: Check imprint link
	Given I see the "JePySi title link"
	And I see a "imprint link"
	When I click the "imprint link"
	Then I should see the "imprint" title after 5s

Scenario: Check BitBucket link
	Given I see the "JePySi title link"
	And I see a "Bitbucket link"
	When I click the "Bitbucket link"
	Then I should see the "Bitbucket logo" after 5s
	Then I should be able to close the "Bitbucket logo" tab after 5s

Scenario: Check Bintray link
	Given I see the "JePySi title link"
	And I see a "Bintray link"
	When I click the "Bintray link"
	Then I should see the "Bintray url" after 5s
	Then I should be able to close the "Bintray url" tab after 5s
