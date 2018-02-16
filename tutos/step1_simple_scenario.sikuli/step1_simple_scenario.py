# -*- coding:utf-8 -*-

'''
1 click on the start button
2 type "notepad++"
3 wait for the appropriate icon, and click it
4 click on the new document icon
5 once it's opened, type in "Hello Notepad++, I'm Sikuli"
6 Hit the save button, and type a name for the file (e.g.:
C:\Temp\SikuliTest.txt), then hit "Save".
'''

click("start_button.png")
wait("start_menu_search.png")
paste("notepad++.png")
wait("notepad_icon_start.png")
click("notepad_icon_start.png")
