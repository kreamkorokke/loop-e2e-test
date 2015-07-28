from marionette_driver.by import By
from marionette_driver.errors import NoSuchElementException, StaleElementException
# noinspection PyUnresolvedReferences
from marionette_driver import Wait
from marionette import MarionetteTestCase

import os
import sys
import urlparse
sys.path.insert(1, os.path.dirname(os.path.abspath(__file__)))


class BrowserCallTestRecipient(MarionetteTestCase):

	def setUp(self):
		MarionetteTestCase.setUp(self)

	def tearDown(self):
		MarionetteTestCase.tearDown(self)
