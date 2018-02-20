Assets:
# Common stuff on page
	"chrome browser active" = mac/browser-active.png | win/browser-active.png | linux/browser-active.png
	"browser url field" = browser-urlfield.png
	"Bitbucket link" = link-bitbucket.png
	"arjs.net link" = link-arjsnet.png
	"JePySi title link" = link-jepysi.png
	"imprint link" = link-imprint.png
	"Bintray link" = link-download.png
	"Tested with" = block-tested.png
	"first page" = block-sidebar.png
# Extra check stuff
	"JePySi title" = title-jepysi.png
	"arjs.net company logo" = block-arjsnetlogo.png
	"imprint" = title-imprint.png
	"Bitbucket logo" = mac/logo-bitbucket.png | win/logo-bitbucket.png | linux/logo-bitbucket.png
	"Bintray logo" = logo-bintray.png
	"Bintray url" = mac/url-bintray.png | win/url-bintray.png | linux/url-bintray.png

Constants:
	domain = jepysi.arjs.net

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
	Then I should see the "JePySi title link"

After: Close Browser Tab
	Given I see the "chrome browser active"
	When I close the browser tab
	Then I should not see the "JePySi title link"
