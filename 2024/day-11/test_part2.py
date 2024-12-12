import unittest
from part1 import solve

class TestPart1(unittest.TestCase):
    def test_sample_input(self):
        INPUT = """125 17"""
        result = solve(INPUT)
        self.assertEqual(result, "55312")

if __name__ == "__main__":
    unittest.main()