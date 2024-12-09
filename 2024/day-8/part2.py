import numpy as np
from itertools import combinations

def solve(input_srt):

    lines = input_srt.strip().split("\n")
    grid = np.array([[row for row in line] for line in lines])
    
    copy_grid = grid.copy()
    copy_grid[:] = "."
    visited_chars = set()

    for i in range(grid.shape[0]):
       for j in range(grid.shape[1]):
          if grid[i, j] != '.' and not grid[i, j] in visited_chars:
            visited_chars.add(grid[i, j])
            positions = np.argwhere(grid == grid[i, j])

            pairs = list(combinations(positions, 2))

            place_antinodes(pairs, copy_grid)

    print(grid)
    print(copy_grid)

    positions = np.argwhere(grid != '.')
    # Flatten the positions and place the elements
    for (row, col), value in zip(positions, grid.flatten()):
        copy_grid[row, col] = value

    print(copy_grid)

    count = np.count_nonzero(copy_grid == "#") + np.count_nonzero(grid != '.')
    print(count)

    return str(count)

def place_antinodes(pairs, copy_grid):
    for pair in pairs:
        
        print(pair[0], pair[1])
        to_top = pair[0] - pair[1]
        to_bottom = pair[1] - pair[0]
        
        print(to_top, to_bottom)

        antinode_pos_top = pair[0] + to_top
        antinode_pos_bottom = pair[1] + to_bottom

        top = (0 <= antinode_pos_top[0] <= copy_grid.shape[0] - 1) and (0 <= antinode_pos_top[1] <= copy_grid.shape[0] - 1)
        bottom = (0 <= antinode_pos_bottom[0] <= copy_grid.shape[0] - 1) and (0 <= antinode_pos_bottom[1] <= copy_grid.shape[0] - 1)

        while top or bottom:
        
          print("antinode top pos", antinode_pos_top)
          print("antinode bottom pos", antinode_pos_bottom)

          # place the antinode # to the top pair
          # check first for in bounds
          # if is_inbounds(copy_grid, antinode_pos_top, antinode_pos_bottom):
          t_row_top = antinode_pos_top[0]
          t_col_top = antinode_pos_top[1]
          b_row_bott = antinode_pos_bottom[0]
          b_col_bott = antinode_pos_bottom[1]

          # now if this works as expect we update the grid
          # we have to double check before we place a hash again
          top = (0 <= t_row_top <= copy_grid.shape[0] - 1) and (0 <= t_col_top <= copy_grid.shape[0] - 1)
          bottom = (0 <= b_row_bott <= copy_grid.shape[0] - 1) and (0 <= b_col_bott <= copy_grid.shape[0] - 1)

          print(top, bottom)

          if top:
            copy_grid[t_row_top][t_col_top] = "#"
          if bottom:
              copy_grid[b_row_bott][b_col_bott] = "#"
          
          antinode_pos_top = antinode_pos_top + to_top
          antinode_pos_bottom = antinode_pos_bottom + to_bottom
          print("updated", antinode_pos_top)
          print("updated", antinode_pos_bottom)
          top = (0 <= antinode_pos_top[0] <= copy_grid.shape[0] - 1) and (0 <= antinode_pos_top[1] <= copy_grid.shape[0] - 1)
          bottom = (0 <= antinode_pos_bottom[0] <= copy_grid.shape[0] - 1) and (0 <= antinode_pos_bottom[1] <= copy_grid.shape[0] - 1)

def is_inbounds(copy_grid, a_top, a_bottom):
  row_inbound = (0 <= a_top[0] <= copy_grid.shape[0] - 1) or (0 <= a_bottom[0] <= copy_grid.shape[0] - 1)
  col_inbound = (0 <= a_top[1] <= copy_grid.shape[1] - 1) or (0 <= a_bottom[1] <= copy_grid.shape[1] - 1)

  if row_inbound and col_inbound:
    return True
  
  return False
