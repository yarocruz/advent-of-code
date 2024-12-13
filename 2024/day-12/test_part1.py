import unittest
from part1 import solve

class TestPart1(unittest.TestCase):
    def test_sample_input(self):
        INPUT = """AAAA
BBCD
BBCC
EEEC"""
        result = solve(INPUT)
        self.assertEqual(result, "140")

    def test_sample_input_2(self):
        INPUT = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""
        result = solve(INPUT)
        self.assertEqual(result, "772")

    def test_sample_input_3(self):
        INPUT = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
        result = solve(INPUT)
        self.assertEqual(result, "1930")
if __name__ == "__main__":
    unittest.main()