import unittest
from part1 import solve

class TestPart1(unittest.TestCase):
    def test_sample_input(self):
        INPUT = """2333133121414131402"""
        result = solve(INPUT)
        self.assertEqual(result, "1928")

if __name__ == "__main__":
    unittest.main()