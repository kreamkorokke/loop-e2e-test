#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pexpect
import sys
import re


def clean_up_message_logs(client):
	# clean up the previous message logs
	messages = client.messages.list()
	for i in range(0, len(messages)):
		client.messages.delete(messages[i].sid)

def run_msisdn_cli(client, cli_command, gateway_number, test_number):
	# spawn a worker for msisdn-cli
	worker = pexpect.spawn("bash")
	worker.logfile = sys.stdout
	worker.sendline("cd ./msisdn-cli; virtualenv .venv; . .venv/bin/activate; python ./setup.py develop")
	worker.sendline(cli_command)
	print("Executing command: " + cli_command)

	# retrieve the verification message
	worker.expect("Please\senter\sthe\scode\sthat\syou\swill\sget\sby\sSMS\sfrom\s")
	message_log = client.messages.list(gateway_number, test_number, time.strftime("%Y-%m-%d", time.gmtime()))
	while not message_log:
		time.sleep(1)
		message_log = client.messages.list(gateway_number, test_number, time.strftime("%Y-%m-%d", time.gmtime()))
	verification_message = message_log[0].body

	# extract the code
	match = re.search("^Your\sverification\scode\sis:\s(\d\d\d\d\d\d)", verification_message)
	worker.sendline(match.group(1))
	worker.expect("Verified")
	print("++++++++++++++++++++ Number: " + test_number + " VERIFIED +++++++++++++++++++")

def main():
	caller = pexpect.spawn("bash")
	caller.logfile = sys.stdout
	caller.sendline("")

if __name__ == "__main__":
	main()