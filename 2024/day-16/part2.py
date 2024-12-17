from collections import deque
import math
import heapq

def solve(input_srt):
    lines = input_srt.splitlines()
    maze = [[c for c in line] for line in lines]

    rows = len(maze)
    cols = len(maze[0]) if rows > 0 else 0

    # start with dummy values
    start_cell = (0, 0)
    end_cell = (0, 0)
    
    #find start and end
    for row in range(rows):
        for col in range(cols):
            if maze[row][col] == "S":
                start_cell = (row, col)
            if maze[row][col] == "E":
                end_cell = (row, col)

    deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    start_direction = 1

    # Infinity
    INF = float('inf')
    # dist[row][col][dir] = minimal cost to reach (row,col) with direction dir
    dist = [[[INF for _ in range(4)] for _ in range(cols)] for _ in range(rows)]
    # the starting state
    dist[start_cell[0]][start_cell[1]][start_direction] = 0
    pq = []
    heapq.heappush(pq, (0, start_cell[0], start_cell[1], start_direction))

    # Dijkstra's algorithm
    while pq:
        curr_cost, r, c, d = heapq.heappop(pq)

        # If this cost is outdated, skip
        if curr_cost > dist[r][c][d]:
            continue

        # Check if we reached the end
        if (r, c) == end_cell:
            # curr_cost is the minimal cost to reach the end
            pass

        # Move forward
        nr, nc = r + deltas[d][0], c + deltas[d][1]
        if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#':
            forward_cost = curr_cost + 1
            if forward_cost < dist[nr][nc][d]:
                dist[nr][nc][d] = forward_cost
                heapq.heappush(pq, (forward_cost, nr, nc, d))

        # Rotate clockwise
        nd_clockwise = (d + 1) % 4
        rotate_cost_cw = curr_cost + 1000
        if rotate_cost_cw < dist[r][c][nd_clockwise]:
            dist[r][c][nd_clockwise] = rotate_cost_cw
            heapq.heappush(pq, (rotate_cost_cw, r, c, nd_clockwise))

        # Rotate counterclockwise
        nd_ccw = (d + 3) % 4
        rotate_cost_ccw = curr_cost + 1000
        if rotate_cost_ccw < dist[r][c][nd_ccw]:
            dist[r][c][nd_ccw] = rotate_cost_ccw
            heapq.heappush(pq, (rotate_cost_ccw, r, c, nd_ccw))

    # Find the minimal cost to reach end_cell in any direction
    er, ec = end_cell
    min_cost = min(dist[er][ec])

    # Now we backtrack to find all states that are part of ANY minimal-cost path
    # We'll do a reverse search: from all minimal end states, find all that can lead to them
    best_path_tiles = [[False]*cols for _ in range(rows)]
    visited_states = [[[False]*4 for _ in range(cols)] for _ in range(rows)]

    # Start from all end states with minimal cost
    queue = deque()
    for d in range(4):
        if dist[er][ec][d] == min_cost:
            queue.append((er, ec, d))
            visited_states[er][ec][d] = True
            best_path_tiles[er][ec] = True

    # Reverse transitions:
    # Forward move reversed: If we ended up at (nr,nc,d) from (r,c,d) with +1 cost,
    # then (r,c,d) can lead to (nr,nc,d). Reversed: (r,c,d) <- (nr,nc,d) if dist[r][c][d]+1=dist[nr][nc][d].
    #
    # Rotation reversed: If we ended up at (r,c,d_cw/ccw) from (r,c,d) with +1000 cost,
    # then reversed: (r,c,d) <- (r,c,d_rot) if dist[r][c][d]+1000=dist[r][c][d_rot].

    while queue:
        r, c, d = queue.popleft()
        curr_dist = dist[r][c][d]

        # Check who can move forward into (r,c,d)
        # If we moved forward to get here, we came from (r - delta[d], c - delta[d], d)
        pr, pc = r - deltas[d][0], c - deltas[d][1]
        if 0 <= pr < rows and 0 <= pc < cols and maze[pr][pc] != '#':
            # If dist[pr][pc][d] + 1 == dist[r][c][d], then (pr,pc,d) is on a best path
            if dist[pr][pc][d] + 1 == curr_dist:
                if not visited_states[pr][pc][d]:
                    visited_states[pr][pc][d] = True
                    best_path_tiles[pr][pc] = True
                    queue.append((pr, pc, d))

        # Check rotations: If we rotated to get here, we can reverse that rotation
        # If (r,c,d) came from (r,c,d_rot) by a rotation cost of 1000:
        # Clockwise rotation means d_rot = (d - 1) % 4
        d_ccw = (d + 3) % 4  # The direction from which we came if we rotated clockwise
        if dist[r][c][d_ccw] + 1000 == curr_dist:
            if not visited_states[r][c][d_ccw]:
                visited_states[r][c][d_ccw] = True
                best_path_tiles[r][c] = True
                queue.append((r, c, d_ccw))

        # Counterclockwise rotation means d_rot = (d + 1) % 4
        d_cw = (d + 1) % 4
        if dist[r][c][d_cw] + 1000 == curr_dist:
            if not visited_states[r][c][d_cw]:
                visited_states[r][c][d_cw] = True
                best_path_tiles[r][c] = True
                queue.append((r, c, d_cw))

    # Now best_path_tiles[r][c] == True means this tile is on at least one best path
    count_best_path_tiles = sum(sum(1 for c in row if c) for row in best_path_tiles)

    return str(count_best_path_tiles)

def score_paths(points):
    score = 0
    directions = []

    for i in range(1, len(points)):
        # compute direction
        dx = points[i][0] - points[i - 1][0]
        dy = points[i][1] - points[i - 1][1]

        if dx != 0:
            direction = (dx // abs(dx), 0)
        else:
            direction = (0, dy // abs(dy))

        directions.append(direction)

        if i > 1 and directions[-1] != directions[-2]:
            score += 1000
        
        score += 1
    
    return score + 1000

def find_all_paths(maze, start, end):
    """
    Finds all paths in a maze from start to end.

    Args:
        maze: A 2D list representing the maze (0: path, 1: wall).
        start: A tuple (row, col) representing the start position.
        end: A tuple (row, col) representing the end position.

    Returns:
        A list of lists, where each inner list is a path (list of tuples).
    """

    min_score = math.inf

    def is_valid(row, col):
        return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != "#"

    all_paths = []
    queue = deque([(start, [start])])
    
    while queue:
        current, path = queue.popleft()
        row, col = current

        if current == end:
            score = score_paths(path)
            if score < min_score:
                min_score = score
            else:
                break

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_row, next_col = row + dr, col + dc
            next_cell = (next_row, next_col)
            
            if (is_valid(next_row, next_col) and 
                next_cell not in path):
                new_path = path + [next_cell]
                queue.append((next_cell, new_path))

    return min_score

def shortest_path_bfs(maze, start, end):
    """
    Finds the shortest path in a maze using BFS.

    Args:
        maze: A 2D list representing the maze, where 0 is a path and 1 is a wall.
        start: A tuple (row, col) representing the starting cell.
        end: A tuple (row, col) representing the ending cell.

    Returns:
        The length of the shortest path, or -1 if no path exists.
    """

    rows, cols = len(maze), len(maze[0])
    queue = deque([start])
    visited = [[False] * cols for _ in range(rows)]
    distance = [[-1] * cols for _ in range(rows)]

    visited[start[0]][start[1]] = True
    distance[start[0]][start[1]] = 0

    while queue:
        row, col = queue.popleft()

        if (row, col) == end:
            return distance[row][col]

        # Explore neighbors (up, down, left, right)
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        for nr, nc in neighbors:
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != "#" and not visited[nr][nc]:
                queue.append((nr, nc))
                visited[nr][nc] = True
                distance[nr][nc] = distance[row][col] + 1

    return -1  # No path found