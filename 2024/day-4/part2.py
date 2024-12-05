import numpy as np

def solve(input_srt):
    lines = input_srt.strip().split("\n")
    grid = np.array([[row for row in line] for line in lines])
    result = 0
    
    
    # this one we need to change tactic
    # for every A look up to it's diags to see if they spell MAS
    # if they do count that as an X-MAS
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row][col] == 'A':
                # check for out of bounds
                row_in_bounds = row > 0 and row < grid.shape[0] - 1
                col_in_bounds = col > 0 and col < grid.shape[1] - 1

                if row_in_bounds and col_in_bounds:
                    if is_x_cross(grid, row, col):
                        result += 1

    return str(result)

def is_x_cross(grid, row, col):
    # check for out of bounds
    top = row - 1
    left = col - 1
    bottom = row + 1
    right = col + 1

    right_left_diag = grid[top][left] == 'M' and grid[bottom][right] == 'S' or grid[top][left] == 'S' and grid[bottom][right] == 'M'
    left_right_diag = grid[top][right] == 'M' and grid[bottom][left] == 'S' or grid[top][right] == 'S' and grid[bottom][left] == 'M'

    if right_left_diag and left_right_diag:
        return True

    return False

