import numpy as np
import re
import sys

np.set_printoptions(threshold=sys.maxsize, linewidth=150)

def solve(input_srt):
    lines = input_srt.splitlines()

    # for the test input, our grid to check the 
    # robot movements our going to be an 11, 7 grid

    # the real grid 101, 103

    # extract the robot positions and velocities
    pos_vel = [re.findall("-*\d+", line) for line in lines]
    robots = np.array([[(int(pos[1]), int(pos[0])), (int(pos[3]), int(pos[2]))] for pos in pos_vel])

    # create test tile grid
    tile_grid = np.full((103, 101), 0)
    #print(tile_grid)
    row_size = tile_grid.shape[0] - 1
    col_size = tile_grid.shape[1] - 1

    # now in the tile grid we place the robots in their initial positions
    for i in range(7000):
      # i think we need to reset all to zeroes here
      tile_grid = np.full((103, 101), '.')
      for idx, pos in enumerate(robots):
          p, v = pos

          # reset previous pos to 0's
          #tile_grid[p[0], p[1]] = 0
          
          new_rp = p[0] + v[0]
          new_cp = p[1] + v[1]

          # we need to go around, backwards or forward if we get out of bounds indexes
          if new_rp > row_size:
              new_rp = new_rp - row_size - 1
          if new_cp > col_size:
              new_cp = new_cp - col_size - 1
          if new_rp < 0:
              new_rp =  row_size + new_rp + 1
          if new_cp < 0:
              new_cp =  col_size + new_cp + 1

          if tile_grid[new_rp, new_cp] == '.':
              tile_grid[new_rp, new_cp] = "#"
          

          # update the postion tuple
          robots[idx] = [(new_rp, new_cp), v]
      
      # Let's the Christmas Tree shape:
      # print("------------------------")
      # print(f"Whe are at second: {i}")
      # for line in tile_grid:
      #     print("".join(line))
      # print("------------------------")

      # lets try writing a file
      with open("myfile.txt", "a") as file:
        file.write("------------------------\n")
        file.write(f"Whe are at second: {i}\n")
        for line in tile_grid:
          l = "".join(line)
          file.write(f"{l}\n")
        file.write("------------------------\n")

    # print(tile_grid)

    # # now we split the tile_grid into quadrants
    # mid_row_idx = tile_grid.shape[0] // 2
    # mid_col_idx = tile_grid.shape[1] // 2

    # # del mid row and col
    # row_deleted = np.delete(tile_grid, mid_row_idx, axis=0)
    # quadrant = np.delete(row_deleted, mid_col_idx, axis=1)

    # # split into 4 different quadrants
    # h_quad = np.vsplit(quadrant, 2)
    # quad = [np.hsplit(h, 2) for h in h_quad]
    
    # result = 1

    # #print(quad)

    # for half in quad:
    #     for h in half:
    #         total = np.sum(h)
    #         result *= total

    # return str(result)

