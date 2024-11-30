import unittest
from part1 import solve

class TestPart1(unittest.TestCase):
    def test_sample_input(self):
        INPUT = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
        result = solve(INPUT)
        self.assertEqual(result, "142")

if __name__ == "__main__":
    unittest.main()