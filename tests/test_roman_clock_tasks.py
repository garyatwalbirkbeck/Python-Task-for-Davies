import unittest
from roman_clock_tasks.roman_converter import roman_to_int, int_to_roman, is_valid_roman_numeral
from roman_clock_tasks.word_reverser import reverse_words
from roman_clock_tasks.clock_angle import calculate_clock_angle

class TestRomanConverter(unittest.TestCase):
    def test_roman_to_int_valid(self):
        test_cases = [
            ("I", 1),
            ("IV", 4),
            ("IX", 9),
            ("XLIX", 49),
            ("XCIX", 99),
            ("CMXCIX", 999),
            ("MCMXC", 1990),
            ("MMVIII", 2008),
            ("MDCLXVI", 1666),
        ]
        for roman, expected in test_cases:
            with self.subTest(roman=roman):
                self.assertEqual(roman_to_int(roman), expected)

    def test_roman_to_int_invalid(self):
        invalid_cases = ["IIII", "VV", "IC", "MMMM", "XCXC", "CMCM"]
        for invalid in invalid_cases:
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    roman_to_int(invalid)

    def test_int_to_roman_valid(self):
        test_cases = [
            (1, "I"),
            (4, "IV"),
            (9, "IX"),
            (49, "XLIX"),
            (99, "XCIX"),
            (999, "CMXCIX"),
            (1990, "MCMXC"),
            (2008, "MMVIII"),
            (1666, "MDCLXVI"),
        ]
        for num, expected in test_cases:
            with self.subTest(num=num):
                self.assertEqual(int_to_roman(num), expected)

    def test_int_to_roman_invalid(self):
        invalid_cases = [0, 4000, -1, 10000]
        for invalid in invalid_cases:
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    int_to_roman(invalid)

    def test_is_valid_roman_numeral(self):
        valid_cases = ["IV", "IX", "XLIX", "XCIX", "CMXCIX", "MCMXC", "MMVIII"]
        invalid_cases = ["IIII", "VV", "IC", "MMMM", "XCXC", "CMCM", "MCMC"]
        
        for valid in valid_cases:
            with self.subTest(valid=valid):
                self.assertTrue(is_valid_roman_numeral(valid))
        
        for invalid in invalid_cases:
            with self.subTest(invalid=invalid):
                self.assertFalse(is_valid_roman_numeral(invalid))

    def test_roundtrip_conversion(self):
        for num in range(1, 4000):
            with self.subTest(num=num):
                roman = int_to_roman(num)
                self.assertEqual(roman_to_int(roman), num)

class TestWordReverser(unittest.TestCase):
    def test_reverse_words(self):
        test_cases = [
            ("Hello World", "olleH dlroW"),
            ("Python is awesome", "nohtyP si emosewa"),
            ("12345 67890", "54321 09876"),
            ("a b c d e", "a b c d e"),
            ("", ""),
        ]
        for input_str, expected in test_cases:
            with self.subTest(input_str=input_str):
                self.assertEqual(reverse_words(input_str), expected)

    def test_reverse_words_with_punctuation(self):
        test_cases = [
            ("Hello, World!", "olleH, dlroW!"),
            ("Python: A Programming Language", "nohtyP: A gnimmargorP egaugnaL"),
            ("Reverse... these words!", "esreveR... eseht sdrow!"),
        ]
        for input_str, expected in test_cases:
            with self.subTest(input_str=input_str):
                self.assertEqual(reverse_words(input_str), expected)

class TestClockAngle(unittest.TestCase):
    def test_calculate_clock_angle(self):
        test_cases = [
            ((3, 0), 90),
            ((6, 0), 180),
            ((12, 0), 0),
            ((5, 30), 15),
            ((9, 45), 22.5),
        ]
        for (hours, minutes), expected in test_cases:
            with self.subTest(hours=hours, minutes=minutes):
                self.assertAlmostEqual(calculate_clock_angle(hours, minutes), expected, places=1)

    def test_calculate_clock_angle_invalid(self):
        invalid_cases = [
            (24, 0),
            (12, 60),
            (-1, 30),
            (10, -15),
        ]
        for hours, minutes in invalid_cases:
            with self.subTest(hours=hours, minutes=minutes):
                with self.assertRaises(ValueError):
                    calculate_clock_angle(hours, minutes)

if __name__ == "__main__":
    unittest.main()