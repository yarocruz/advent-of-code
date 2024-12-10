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
  def find_reachable_nines(x, y, current_value, visited, reached_nines):
      if grid[x, y] == 9:  # If we reach a 9, add its position to the set
          reached_nines.add((x, y))
          return

      visited[x, y] = True  # Mark the cell as visited
      next_value = current_value + 1  # Next number in the sequence

      # Explore all valid moves
      for dx, dy in directions:
          nx, ny = x + dx, y + dy
          if is_valid(nx, ny, visited, next_value):
              find_reachable_nines(nx, ny, next_value, visited, reached_nines)

      visited[x, y] = False  # Backtrack: unmark the cell
  
  # Function to count unique 9's reachable from a specific 0
  def count_reachable_nines(grid, start_x, start_y):
      visited = np.zeros_like(grid, dtype=bool)  # Track visited cells
      reached_nines = set()  # Set to track unique 9's
      find_reachable_nines(start_x, start_y, current_value=0, visited=visited, reached_nines=reached_nines)
      return len(reached_nines)

    
  # find all the 0's in grid
  start_positions = np.argwhere(grid == 0)

  total = 0
  for x, y in start_positions:
    total += count_reachable_nines(grid, x, y)
    #print(total_paths)

  print(total)
    
  return str(total)