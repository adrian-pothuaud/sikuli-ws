Assets:
	"<items>" = item-u-:item:.png
	"highlighted <items>" = item-s-:item:.png

Environments:
	PROD	: url = http://www.werk1muenchen.de/


Feature: Check if the menu structure is viewed correctly
	As a website owner I want to see a working menu structure,
	when I hover over the menu section on the top of the page,
	I want to see the sub menu open and the item selected,
	so I'm sure the users get the full experience.


Scenario Outline: Check submenu elements
	Given I see the "#logo# logo" at the top
	And I see a "top menu"
	When I hover the "<menu> item"
	Then I should see the "<submenu> submenu" block
	And I should be able to hover over the "<items>" submenu items and see it highlighted

Examples: Submenus
	| menu		| submenu	| items															|
	| Werk1		| Werk1 	| philosophie, standort, mieter, anfahrt						|
	| Startups	| Startups	| philosophie, mieterinfos, networking, beratung, mietanfrage	|
	| Coworking	| Coworking | philosophie, iup												|
	| Events	| Events	| philosophie, eventkalender, eventarchiv, werk1-m, location	|
