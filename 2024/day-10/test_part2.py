import unittest
from part2 import solve

class TestPart1(unittest.TestCase):
    def test_sample_input(self):
        INPUT = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""
        result = solve(INPUT)
        self.assertEqual(result, "81")

if __name__ == "__main__":
    unittest.main()