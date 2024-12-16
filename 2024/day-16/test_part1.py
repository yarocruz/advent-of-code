import unittest
from part1 import solve

class TestPart1(unittest.TestCase):
    def test_sample_input(self):
        INPUT = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""
        result = solve(INPUT)
        self.assertEqual(result, "7036")
    

if __name__ == "__main__":
    unittest.main()