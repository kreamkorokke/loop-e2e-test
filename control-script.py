#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pexpect
import sys
import re

def main():
	# spin up the caller test case and get the room url
	caller = pexpect.spawn("bash")
	caller.logfile = sys.stdout
	caller.sendline("cd ../firefox-42.0a1.en-US.mac.tests/marionette/marionette; python runtests.py --binary=/Applications/Firefox.app/Contents/MacOS/firefox-bin --address=localhost:2828 --type=browser ../../../loop-e2e-test/caller_case.ini")
	caller.expect("Give a GO sign")
	match = re.search("The\sroom\surl\sis:\s(http.+)", caller.before)
	room_url = match.group(1)

	# spin up the recipient test case to join the room
	recipient = pexpect.spawn("bash")
	recipient.logfile = sys.stdout
	recipient.sendline("cd ../firefox-42.0a1.en-US.mac.tests/marionette/marionette; python runtests.py --binary=/Applications/Firefox.app/Contents/MacOS/firefox-bin --address=localhost:2829 --type=browser ../../../loop-e2e-test/recipient_case.ini")
	recipient.sendline(room_url)
	recipient.expect("Done?")

	# room established, kill test cases
	caller.sendline("GO")
	recipient.sendline("done")

if __name__ == "__main__":
	main()