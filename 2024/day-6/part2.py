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
    grid[x, y] = '.'

    # return true if guard gets stuck in a loop, false if not
    def simulation(grid):
        gx, gy = x, y
        gdir = direction_state
        visited_states = set()

        visited_states.add((gx, gy, gdir))

        while True:
            dx, dy = deltas[gdir]   
            next_x = gx + dx
            next_y = gy + dy

            if not (0 <= next_x < grid.shape[0] and 0 <= next_y < grid.shape[1]):
                return False

            if grid[next_x, next_y] == "#":
                dir_index = directions.index(gdir)
                gdir = directions[(dir_index + 1) % 4]
            else: 
                gx, gy = next_x, next_y

            current_state = (gx, gy, gdir)
            if current_state in visited_states:
                return True
            visited_states.add(current_state)

    loop_count = 0

    # save starting position of "guard" to avoid placing obstacles in that position
    start_pos = (x, y)

    rows, cols = grid.shape
    for i in range(rows):
        for j in range(cols):
            if (i, j) != start_pos and grid[i, j] == '.':
                # place a temp obstruction
                original_char = grid[i, j]
                grid[i, j] = "#"

                if simulation(grid):
                    loop_count += 1
                
                # restore back the char for next loop(s)
                grid[i, j] = original_char

    return str(loop_count)

