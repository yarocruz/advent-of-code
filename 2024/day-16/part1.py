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
            return str(curr_cost)

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

    # If we exit the loop without returning, it means there's no path
    return str(-1)

    return str("")

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