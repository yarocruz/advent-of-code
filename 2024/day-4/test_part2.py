import unittest
from part2 import solve

class TestPart1(unittest.TestCase):
    def test_sample_input(self):
        INPUT = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""
        result = solve(INPUT)
        self.assertEqual(result, "9")

if __name__ == "__main__":
    unittest.main()