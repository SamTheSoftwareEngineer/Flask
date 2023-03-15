"""Example of unit tests."""

import arithmetic
# Import unittest from standard library and testCase 
from unittest import TestCase

# Inherits from the testcase class 
class AdditionTestCase(TestCase):
    """Examples of unit tests."""
# must start with test_
    def test_adder(self):
        assert arithmetic.adder(2, 3) == 5

    def test_adder_2(self):
        # instead of assert arithmetic.adder(2, 2) == 4
        self.assertEqual(arithmetic.adder(2, 2), 4)
        self.assertEqual(arithmetic.adder(40,50), 90)
        