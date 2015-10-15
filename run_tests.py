#!/usr/bin/env python

import unittest

from src.convert import kilometers_to_miles, miles_to_kilometers, \
years_to_minutes, minutes_to_years

class TestConvert(unittest.TestCase):
    def test_km_to_miles(self):
        acutal = kilometers_to_miles(1)
        expected = 0.621 # general knowledge
        #self.assertAlmostEqual(acutal, expected, delta = 0.01)
        
    def test_miles_to_km(self):
        actual = mile_to_kilometers(1)
        expected = 1.609 # general knowledge
        self.assertAlmostEqual(actual, expected, delta = 0.01)
      
    def test_years_to_minutes(self):
        actual = 525600 #general knowledge
        self.assertEqual(actual, years_to_minutes(1))
        
    def test_minutes_to_years(self):
        self.assertEqual(1, minutes_to_years(525600))

    def test_inches_to_cm(self):
        self.assertEqual(2.54, inches_to_cm(1))
        
    def test_cm_to_inches(self):
        self.assertAlmostEqual(1, cm_to_inches(1), delta = 0.05)

#######################################################

if __name__ == '__main__':
    unittest.main()
