import unittest
from part2 import solve

class TestPart1(unittest.TestCase):
    def test_sample_input(self):
        INPUT = """2333133121414131402"""
        result = solve(INPUT)
        self.assertEqual(result, "2858")

if __name__ == "__main__":
    unittest.main()