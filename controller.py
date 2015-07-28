#!/usr/bin/python
# launch browser 1 (profile: caller, 2828) and browser 2 (profile: recipient, 2829) 
# OSX:  /Applications/Firefox.app/MacOS/Contents/firefox -CreateProfile caller
# OSX:  /Applications/Firefox.app/MacOS/Contents/firefox -CreateProfile recipient
# when we make marionette launch two browsers, set profiles and repipe their stdout to two files
# caller clicks on hello icon, start a conversation, copies link
# controller script grabs the link, sends it to recipient, 
# recipient paste it into address bar, press return, finds the join button, clicks on it, find shared selected device button, clicks on shared selected device
# vefiry media in caller and recipient
# find leave button in recipient, click it
# verify the conversation ended in caller (by finding text or something else)
# terminate test (done!!!)




