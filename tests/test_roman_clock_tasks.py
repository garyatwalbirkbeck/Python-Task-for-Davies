import unittest
from roman_clock_tasks import roman_to_int, reverse_words, calculate_clock_angle

class TestRomanClockTasks(unittest.TestCase):
    def test_roman_to_int(self):
        self.assertEqual(roman_to_int("MCMXC"), 1990)
        self.assertEqual(roman_to_int("MMVIII"), 2008)
        self.assertEqual(roman_to_int("MDCLXVI"), 1666)
        with self.assertRaises(ValueError):
            roman_to_int("INVALID")

    def test_reverse_words(self):
        self.assertEqual(reverse_words("Hello World"), "olleH dlroW")
        self.assertEqual(reverse_words("Python is awesome"), "nohtyP si emosewa")
        self.assertEqual(reverse_words(""), "")

    def test_calculate_clock_angle(self):
        self.assertAlmostEqual(calculate_clock_angle(3, 0), 90.0)
        self.assertAlmostEqual(calculate_clock_angle(12, 0), 0.0)
        self.assertAlmostEqual(calculate_clock_angle(5, 30), 15.0)
        with self.assertRaises(ValueError):
            calculate_clock_angle(24, 60)

if __name__ == "__main__":
    unittest.main()