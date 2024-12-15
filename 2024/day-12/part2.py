import numpy as np

def solve(input_srt):
  lines = input_srt.strip().split("\n")
  grid = np.array([[row for row in line.strip()] for line in lines])

  regions = find_connected_components(grid)

  for rid, info in regions.items():
    visited = set()
    perimeter_count = 0
    if is_four_sided(info['cells']):
      perimeter_count += 4
    else:
       for x, y in info['cells']:
          perimeter_count += count_sides(info['char'], grid, x, y, visited)
    info['perimeter'] = perimeter_count

  total = 0
  for r_id, info in regions.items():
     print(f"Region {rid}: Character = {info['char']}, Size = {info['size']}, Perimeter = {info['perimeter']}, Cells = {info['cells']}")
     total += info['size'] * info['perimeter']

  print(total)

  return str(total)

def get_neighbors(r, c, max_r, max_c):
    """Returns valid, orthogonally adjacent neighbors for cell (r, c)."""
    neighbors = []
    for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
        if 0 <= nr < max_r and 0 <= nc < max_c:
            neighbors.append((nr, nc))
    return neighbors

def find_connected_components(grid):
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    
    region_id = 0
    regions = {}  # key: region_id, value: dict with {'char': 'O'/'X', 'cells': [(r,c),...]}
    
    for r in range(rows):
        for c in range(cols):
            if not visited[r, c]:
                # Found a new region start
                region_char = grid[r, c]
                region_id += 1
                
                # BFS/DFS to explore the region
                stack = [(r, c)]
                region_cells = []
                
                while stack:
                    cr, cc = stack.pop()
                    if visited[cr, cc]:
                        continue
                    visited[cr, cc] = True
                    region_cells.append((cr, cc))
                    
                    # Check neighbors of the same character
                    for nr, nc in get_neighbors(cr, cc, rows, cols):
                        if not visited[nr, nc] and grid[nr, nc] == region_char:
                            stack.append((nr, nc))
                
                # Store the region details
                regions[region_id] = {
                    'char': region_char,
                    'cells': region_cells,
                    'size': len(region_cells)
                }

    return regions

def count_sides(letter, grid, x, y, visited):
  # if the letter to the right, left, up, or down is a different letter
  # count that as a perimeter edge
  # *note, top, botom, first col, and last col have respective perimters
  count = 0
  
  # if we are in top row, we can count a top perimeter
  if x == 0:
    count += 1
    
  # if we are in bottom row, we can count a bottom perimeter  
  if x == len(grid) - 1:
    count += 1
    
  # if we are at first col, we can ocunt a left perimeter
  if y == 0:
    count += 1
    
  # if last col, we can count a right perimeter  
  if y == len(grid[0]) - 1:
    count += 1
    

  row_inbound = (0 < x < len(grid) - 1)
  col_inbound = (0 < y < len(grid[0]) - 1)

  if row_inbound:
    if grid[x + 1][y] != letter and not x + 1 in visited:
      visited.add(x + 1)
      count += 1 
    if grid[x - 1][y] != letter and x - 1 in visited:
      visited.add(x - 1)
      count += 1

  if col_inbound:
    if grid[x][y + 1] != letter and y + 1 in visited:
      visited.add(y + 1)
      count += 1
    if grid[x][y - 1] != letter and y - 1 in visited:
      visited.add(y - 1)
      count += 1
  # # now we look up, down, left, right to see if it's different letter
  # if row_inbound or col_inbound:
      
  return count

def is_four_sided(points):
    if not points:
        return False
    
    # Convert to numpy array for convenience
    pts = np.array(points, dtype=int)
    
    min_x, max_x = pts[:,0].min(), pts[:,0].max()
    min_y, max_y = pts[:,1].min(), pts[:,1].max()
    
    # Compute the required area for a fully filled rectangle
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    required_area = width * height
    
    # Convert points to a set for O(1) membership checks
    point_set = set(points)
    
    # Check if all points in bounding rectangle are present
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            if (x, y) not in point_set:
                return False  # Missing a point in the rectangle
    
    # If we got here, it's a fully filled rectangle
    return True