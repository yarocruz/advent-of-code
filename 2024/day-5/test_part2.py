import unittest
from part2 import solve

class TestPart1(unittest.TestCase):
    def test_sample_input(self):
        INPUT = """
"""
        result = solve(INPUT)
        self.assertEqual(result, "123")

if __name__ == "__main__":
    unittest.main()