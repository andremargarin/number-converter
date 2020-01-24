import unittest
from converter import Converter


class TestConverter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.converter = Converter()

    def test_positive_low_numbers(self):
        for n in range(0, 20):
            self.assertEqual(self.converter.translate(n), self.converter.low_numbers[n])

    def test_negative_low_numbers(self):
        for n in range(-19, 0):
            self.assertEqual(
                self.converter.translate(n),
                f'menos {self.converter.low_numbers[abs(n)]}'
            )

    def test_positive_mid_numbers(self):
        values = zip(range(2, 10), self.converter.middle_numbers)
        for value, string in values:
            self.assertEqual(value, string)

    def test_high_numbers(self):
        self.assertEqual(self.converter.translate(2000), 'dois mil')
        self.assertEqual(self.converter.translate(2001), 'dois mil e um')
        self.assertEqual(self.converter.translate(2022), 'dois mil e vinte e dois')
        self.assertEqual(self.converter.translate(2111), 'dois mil e cento e onze')
        self.assertEqual(self.converter.translate(40404), 'quarenta mil e quatrocentos e quatro')
        self.assertEqual(self.converter.translate(22222), 'vinte e dois mil e duzentos e vinte e dois')

    def test_edge_cases(self):
        self.assertEqual(self.converter.translate(0), 'zero')
        self.assertEqual(self.converter.translate(-1000), 'menos mil')
        self.assertEqual(self.converter.translate(1000), 'mil')
