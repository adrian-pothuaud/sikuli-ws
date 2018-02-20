Test Root Folder
========

## Structure

* test/
	+ config/ - Configuration
  		+ config.txt - Global configurations
  		+ LINUX/
    		+ config.txt - Linux specific configuration
  		+ MAC/
    		+ config.txt - Mac specific configuration
  		+ WIN/
    		+ config.txt - Windows specific configuration
	+ features/ - Gherkin style feature files, ending with .feature
	+ images/ - PNG screenshots for sikuli; Should be taken with the Sikuli IDE
		+ linux - Linux specific images
		+ mac - Mac specific images
		+ win - Windows specific images
	+ `runner.sikuli/` - JePySi core system scripts writen in Python; Subject to changes
	+ steps/ - The Python step files with the steps referenced in the feature files

### Remark
`runner.sikuli/` must be copied from jepysi test folder. It isn't supplied within the examples folders

## Run tests

		<path to sikuli script>runScript -r runner [-f <logfile for sikuli>] -- <Environment> <feature oder feature path>

`Important remark`: No wildcard support for feature files or folders
	 
