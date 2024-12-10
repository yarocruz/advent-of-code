import numpy as np
from itertools import combinations

def solve(input_srt):
  lines = input_srt.strip().split("\n")
  grid = np.array([[int(row) for row in line] for line in lines])

  # grid = np.array([
  #   [0, 1, 2, 3],
  #   [1, 2, 3, 4],
  #   [8, 7, 6, 5],
  #   [9, 8, 7, 6]
  # ])

  # Let's get dimensions of grid
  rows, cols = grid.shape

  # up, down, left, right
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

  # checker for out of bounds indexes and visited pos
  def is_valid(x, y, visited, next_value):
    return (
      0 <= x < rows and 
      0 <= y < cols and 
      not visited[x, y] and 
      grid[x, y] == next_value)
  
  # Recursive function to find all reachable 9's
  def count_paths(x, y, current_value, visited, target):
      if grid[x, y] == target:  
          return 1

      visited[x, y] = True  # Mark the cell as visited
      next_value = current_value + 1  # Next number in the sequence
      path_count = 0

      # Explore all valid moves
      for dx, dy in directions:
          nx, ny = x + dx, y + dy
          if is_valid(nx, ny, visited, next_value):
              path_count += count_paths(nx, ny, next_value, visited, target)

      visited[x, y] = False  # Backtrack: unmark the cell
      return path_count
  
  # Function to count unique 9's reachable from a specific 0
  def find_paths_from_zero(grid, start_x, start_y):
      visited = np.zeros_like(grid, dtype=bool)  # Track visited cells
      total_paths = count_paths(start_x, start_y, current_value=0, visited=visited, target=9)
      return total_paths

    
  # find all the 0's in grid
  start_positions = np.argwhere(grid == 0)

  total = 0
  for x, y in start_positions:
    total += find_paths_from_zero(grid, x, y)
    #print(total_paths)

  print(total)
    
  return str(total)