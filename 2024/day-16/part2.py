import numpy as np
import re

def solve(input_srt):

    return str("")

### taken from google AI Overview
from collections import deque

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
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0 and not visited[nr][nc]:
                queue.append((nr, nc))
                visited[nr][nc] = True
                distance[nr][nc] = distance[row][col] + 1

    return -1  # No path found


if __name__ == '__main__':
    # Example maze (0: path, 1: wall)
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    start_cell = (0, 0)
    end_cell = (4, 4)

    shortest_path = shortest_path_bfs(maze, start_cell, end_cell)

    if shortest_path != -1:
        print(f"Shortest path length: {shortest_path}")
    else:
        print("No path found.")
    

