"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

#from django.test import TestCase
import unittest
#from TraderApp.listing_processor import extract_nouns

class SimpleTest(unittest.TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

#    def can_get_one_noun(self):
#        nouns = extract_nouns("car")
#        self.assertEqual(len(nouns), 1)
#        self.assertEqual(nouns[0], "car")


unittest.main()