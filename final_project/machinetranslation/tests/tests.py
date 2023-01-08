import unittest
import translator


class UnitTests(unittest.TestCase):
	def test_english_to_french_hello(self):
		"""Tests translation of hello to French"""
		output = translator.english_to_french("Hello")
		self.assertEqual(output, "Bonjour")
		
	def test_french_to_english_hello(self):
		"""Tests translation of bonjour to English"""
		output = translator.french_to_english("Bonjour")
		self.assertEqual(output, "Hello")
		
	def test_english_to_french_null(self):
		"""Tests exception for translating null to French"""
		with self.assertRaises(translator.NullInputException):
			translator.english_to_french(None)
		
	def test_french_to_english_null(self):
		"""Tests exception for translating null to English"""
		with self.assertRaises(translator.NullInputException):
			translator.french_to_english(None)
		