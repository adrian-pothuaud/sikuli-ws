Assets:
    APP = "Notepad"

Feature: Check the [APP] basics
  As a End-User I want to see the basic elements of [APP],
  when I open the application [APP],
  so I'm sure that the menus are complete.

  Scenario Outline: Check the menu
    Given I have an open [APP]
    When I open the "<menu> menu"
    Then I should see the "<submenu> submenu"

  Examples:
  | menu		| submenu	|
  | file		| new    	|
  | file    | open    |
  | file		| save   	|
  | file    | print   |
