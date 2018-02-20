Assets:
	"<item>" = item-u-<item>.png
	"<page>" = title-<page>.png

Environments:
	PROD	: url = http://www.werk1muenchen.de/

Feature: Check if the imprint page is viewed correctly
	As a website owner I want to see a working menu,
	when I hover over the menu section on the top of the page,
	so I get the full experience.


Scenario Outline: Check submenu elements
	Given I see the "#logo# logo" at the top
	And I see a "top menu"
	When I hover the "<menu> item"
	Then I should see the "<submenu> submenu" block
	And I should be able to click the "<item>" submenu
	And I should be able to see the "<page>" title after 5s

Examples: Pages
	| menu		| submenu	| item			| page 			|
	| Werk1		| Werk1 	| philosophie	| werk1-m 		|
	| Werk1		| Werk1 	| standort		| standort		|
	| Werk1		| Werk1 	| mieter		| mieter		|
	| Werk1		| Werk1 	| anfahrt		| anfahrt		|
	| Startups	| Startups	| philosophie	| startups		|
	| Startups	| Startups	| mieterinfos	| mietinfos 	|
	| Startups	| Startups	| networking	| networking	|
	| Startups	| Startups	| beratung		| beratung		|
	| Startups	| Startups	| mietanfrage	| mieterwerden 	|
	| Coworking	| Coworking | philosophie	| coworking 	|
	| Coworking	| Coworking | iup			| iup 			|
	| Events	| Events	| philosophie	| philosophie	|
	| Events	| Events	| eventkalender	| up-events		|
	| Events	| Events	| eventarchiv	| pa-events 	|
	| Events	| Events	| werk1-m		| werk1-m 		|
	| Events	| Events	| location		| location 		|
