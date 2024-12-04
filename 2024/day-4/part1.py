import numpy as np

def solve(input_srt):
    lines = input_srt.strip().split("\n")
    grid = np.array([[row for row in line] for line in lines])
    print(grid)
    word = "XMAS"
    
    
    # we just need a way to look up down, left-right and diagonally
    # every time we hit on an X, we look 3 down-up, left-right, 4diags
    # if we can of course

    result = count_word_instances(grid, word)
    print(result)

    return str("")

def count_word_instances(grid, word):
    count = 0

    # loop on rows left-to-right, right-to-left
    for row in grid:
        row_str = ''.join(row)
        count += row_str.count(word)
        count += row_str[::-1].count(word)
    
    return count