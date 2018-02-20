Assets:
# Common stuff on page
	"chrome browser active" = mac/browser-active.png | win/browser-active.png | linux/browser-active.png
	"browser url field" = browser-urlfield.png
	"Werk1 logo" = logo-werk1.png
	"top menu" = menu-top.png
	"social menu" = menu-social.png
	"bottom menu" = menu-bottom.png
	"imprint link" = link-imprint.png
	"imprint title" = title-impressum.png
	"Werk1 submenu" = sub-werk1.png
	"Werk1 item" = item-u-werk1.png
	"Startups submenu" = sub-startups.png
	"Startups item" = item-u-startups.png
	"Coworking submenu" = sub-coworking.png
	"Coworking item" = item-u-coworking.png
	"Events submenu" = sub-events.png
	"Events item" = item-u-events.png
	"footer" = block-footer.png
	"facebook like" = button-like.png
	"hotspot link" = block-hotspot.png
	"rss logo" = logo-rss.png
	"twitter logo" = logo-twitter.png
	"facebook logo" = logo-facebook.png
	"press link" = link-press.png
	"events link" = link-events.png
	"mieterinfos link" = link-mieterinfos.png
	"mieterwerden link" = link-mieterwerden.png
	"anfahrt link" = link-anfahrt.png


Constants:
	domain = www.werk1muenchen.de
	logo = Werk1

Setup:
	Given I open a chrome browser
	Then I see the "chrome browser active"
	And I should see "browser url field"

Cleanup:
	Given I see the "chrome browser active"
	And I see the "browser url field"
	When I enter the close app keys
	Then I should not see "chrome browser active"

Before: Open Browser Tab
	Given I see the "chrome browser active"
	And I open a new browser tab
	And I see the "browser url field"
	When I enter [url] into the "browser url field"
	And I press the ENTER Key
	Then I should see the "#logo# logo"

After: Close Browser Tab
	Given I see the "chrome browser active"
	When I close the browser tab
	Then I should not see the "#logo# logo"
