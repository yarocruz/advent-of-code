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

    return str(result)

def count_word_instances(grid, word):
    count = 0

    # loop on rows left-to-right, right-to-left
    for row in grid:
        row_str = ''.join(row)
        count += row_str.count(word)
        count += row_str[::-1].count(word)

    # loop on cols by Transposing: top-bottom, bottom-right
    for col in grid.T:
        col_str = ''.join(col)
        count += col_str.count(word)
        count += col_str[::-1].count(word)

    # loop diag, top-left-bot-right, vice versa
    for offset in range(-grid.shape[0] + 1, grid.shape[1]):
        diag_str = ''.join(grid.diagonal(offset))
        count += diag_str.count(word)
        count += diag_str[::-1].count(word)

    # # loop "anti-diag", top-left-bot-right, vice versa
    flipped_grid = np.fliplr(grid)
    for offset in range(-flipped_grid.shape[0] + 1, flipped_grid.shape[1]):
        diag_str = ''.join(flipped_grid.diagonal(offset))
        count += diag_str.count(word)
        count += diag_str[::-1].count(word)
    
    return count