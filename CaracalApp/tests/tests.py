"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

#https://docs.djangoproject.com/en/dev/topics/testing/overview/
import unittest
from django.test import TestCase
from CaracalApp.listing_processor import extract_nouns
from CaracalApp.SpellChecker import get_correct_spelling

class SimpleTestCase(TestCase):
    def setUp(self):
        pass

    def test_can_get_one_noun_from_one_word(self):
        nouns = extract_nouns("car")
        self.assertEqual(len(nouns), 1)
        self.assertEqual(nouns[0], "car")

    def test_can_get_one_noun_from_noun_phrase(self):
        nouns = extract_nouns("the car")
        self.assertEqual(len(nouns), 1)
        self.assertEqual(nouns[0], "car")

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_speller_good_word(self):
        result = get_correct_spelling("speling")
        self.assertEqual(result, "spelling")

    def test_speller_short_common_word(self):
        result = get_correct_spelling("teh")
        self.assertEqual(result, "the")

    def test_speller_long_common_word(self):
        result = get_correct_spelling("cigarete")
        self.assertEqual(result, "cigarette")

    def test_speller_delete_letter(self):
        result = get_correct_spelling("cigarete")
        self.assertEqual(result, "cigarette")

    def test_speller_insert_letter(self):
        result = get_correct_spelling("cigarrette")
        self.assertEqual(result, "cigarette")

    def test_speller_bad_word(self):
        result = get_correct_spelling("xxxdddd")
        self.assertEqual(result, "xxxdddd")

if __name__ == '__main__':
    unittest.main()