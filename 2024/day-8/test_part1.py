import unittest
from part1 import solve

class TestPart1(unittest.TestCase):
    def test_sample_input(self):
        INPUT = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
        result = solve(INPUT)
        self.assertEqual(result, "14")

if __name__ == "__main__":
    unittest.main()