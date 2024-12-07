import numpy as np

def solve(input_srt):
    lines = input_srt.strip().split("\n")
    grid = np.array([[row for row in line] for line in lines])

    initial_positions = np.where(grid == "^")
    x = initial_positions[0][0]
    y = initial_positions[1][0]

    directions = ["up", "right", "down", "left"]

    direction_state = "up"

    deltas = {
        "up": (-1, 0),
        "right": (0, 1),
        "down": (1, 0),
        "left": (0, -1)
    }

    visited_positions = set()
    visited_positions.add((x, y))
    grid[x, y] = 'X'

    while True:
        dx, dy = deltas[direction_state]   
        next_x = x + dx
        next_y = y + dy

        if not (0 <= next_x < grid.shape[0] and 0 <= next_y < grid.shape[1]):
            break

        if grid[next_x, next_y] == "#":
            curr_dir_index = (directions.index(direction_state)+ 1) % 4
            direction_state = directions[curr_dir_index]
        else: 
            x, y = next_x, next_y
            visited_positions.add((x, y))
            grid[x, y] = 'X'

    return str(len(visited_positions))

