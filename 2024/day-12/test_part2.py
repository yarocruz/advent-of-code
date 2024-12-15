import unittest
from part2 import solve

class TestPart1(unittest.TestCase):
    def test_sample_input(self):
        INPUT = """AAAA
BBCD
BBCC
EEEC"""
        result = solve(INPUT)
        self.assertEqual(result, "80")

    def test_sample_input_2(self):
        INPUT = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""
        result = solve(INPUT)
        self.assertEqual(result, "436")

    def test_sample_input_3(self):
        INPUT = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""
        result = solve(INPUT)
        self.assertEqual(result, "236")


def test_sample_input_4(self):
        INPUT = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""
        result = solve(INPUT)
        self.assertEqual(result, "368")

def test_sample_input_5(self):
        INPUT = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEEA"""
        result = solve(INPUT)
        self.assertEqual(result, "1206")
if __name__ == "__main__":
    unittest.main()