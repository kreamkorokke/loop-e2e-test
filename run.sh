#!/bin/sh

# virtualenv setup
virtualenv marionette_env; source marionette_env/bin/activate
sudo pip install marionette_client
sudo pip install six
sudo pip install pexpect
sudo pip install pyperclip

# run test
python control-script.py


deactivate

sudo rm -fr marionette_env