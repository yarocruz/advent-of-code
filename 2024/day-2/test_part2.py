import unittest
from part2 import solve

class TestPart1(unittest.TestCase):
    def test_sample_input(self):
        INPUT = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
        result = solve(INPUT)
        self.assertEqual(result, "4")

if __name__ == "__main__":
    unittest.main()