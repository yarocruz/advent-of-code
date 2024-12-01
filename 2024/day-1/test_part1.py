import unittest
from part1 import solve

class TestPart1(unittest.TestCase):
    def test_sample_input(self):
        INPUT = """3   4
4   3
2   5
1   3
3   9
3   3"""
        result = solve(INPUT)
        self.assertEqual(result, "11")

if __name__ == "__main__":
    unittest.main()