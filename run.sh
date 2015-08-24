#!/bin/sh +x

# TODO: karl optimization for downloading latest version without needing to hardcode version numbers. :+1:
LATEST_MAC_DMG=$(curl -s ftp://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mozilla-central/ | fgrep en-US.mac.dmg | awk '{print $9}')
curl -# -C - -o './LatestNightly.dmg' "https://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mozilla-central/$LATEST_MAC_DMG"

LATEST_MAC_TESTS=$(curl -s ftp://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mozilla-central/ | fgrep en-US.mac.common.tests.zip | awk '{print $9}')
curl -# -C - -o './mac_tests.zip' "https://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mozilla-central/$LATEST_MAC_TESTS"

# virtualbox setup, assuming that openssh-server is installed in the vm
VBoxManage modifyvm ubuntu-64-marionette --natpf1 "ssh,tcp,,3022,,22"
VBoxManage showvminfo ubuntu-64-marionette | grep 'Rule'

# # ssh into virtualbox and send commands
# VBoxManage startvm ubuntu-64-marionette
# ssh -p 3022 kreamkorokke@127.0.0.1

LATEST_LINUX_DMG=$(curl -s ftp://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mozilla-central/ | fgrep en-US.linux-x86_64.tar.bz2 | awk '{print $9}')
curl -# -C - -o './LatestNightly.tar.bz2' "https://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mozilla-central/$LATEST_LINUX_DMG"

LATEST_LINUX_TESTS=$(curl -s ftp://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mozilla-central/ | fgrep en-US.linux-x86_64.common.tests.zip | awk '{print $9}')
curl -# -C - -o './linux_tests.zip' "https://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mozilla-central/$LATEST_LINUX_TESTS"

# # virtualenv setup
# virtualenv marionette_env; source marionette_env/bin/activate
# sudo pip install marionette_client
# sudo pip install six
# sudo pip install pexpect
# sudo pip install pyperclip

# # run test
# python control-script.py


# deactivate

sudo rm -fr marionette_env
rm LatestNightly.dmg
rm mac_tests.zip
