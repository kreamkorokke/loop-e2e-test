#!/bin/sh

# virtualenv setup
virtualenv marionette_env; source marionette_env/bin/activate
sudo pip install marionette_client
sudo pip install six
sudo pip install pexpect

# python control-script.py



deactivate