import unittest
from converter import Converter


class TestConverter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.converter = Converter()

    def test_low_numbers(self):
        self.assertEqual(self.converter.translate(-1), 'menos um')
        self.assertEqual(self.converter.translate(0), 'zero')
        self.assertEqual(self.converter.translate(2), 'dois')
        self.assertEqual(self.converter.translate(3), 'três')
        self.assertEqual(self.converter.translate(4), 'quatro')

    def test_mid_numbers(self):
        self.assertEqual(self.converter.translate(100), 'cem')
        self.assertEqual(self.converter.translate(200), 'duzentos')
        self.assertEqual(self.converter.translate(300), 'trezentos')

    def test_high_numbers(self):
        self.assertEqual(self.converter.translate(1000), 'mil')
        self.assertEqual(self.converter.translate(2000), 'dois mil')
        self.assertEqual(self.converter.translate(10000), 'dez mil')
        self.assertEqual(self.converter.translate(1234), 'mil e duzentos e trinta e quatro')
        self.assertEqual(self.converter.translate(12345), 'doze mil e trezentos e quarenta e cinco')
