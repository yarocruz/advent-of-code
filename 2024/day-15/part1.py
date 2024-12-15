import numpy as np
import re

def solve(input_srt):
    map, moves = input_srt.strip().split("\n\n")
    moves = moves.replace('\n', "")
    
    # make the map into a 2d grid
    warehouse = np.array([[row for row in line] for line in map.split("\n")])

    # hashes are walls so we can't move
    # our robot can move the boxes

    directions = {
        "<": [0, -1],
        ">": [0, 1],
        "^": [-1, 0],
        "v": [1, 0],
    } 

    # initial robot positions
    robo_position = np.argwhere(warehouse == '@')[0]
    print(robo_position)

    for d in moves:
        move = robo_position + directions[d]

        x, y = move

        if warehouse[x, y] == 'O' and box_is_movable(move, directions[d], warehouse):
            move_box(move, directions[d], warehouse)
            # swap 
            warehouse[x, y] = '@'
            temp = robo_position
            robo_position = move
            # we put . were the robot was
            nx, ny = temp
            warehouse[nx, ny] = '.'
        elif warehouse[x, y] == '.':
            warehouse[x, y] = '@'
            temp = robo_position
            robo_position = move
            # we put . were the robot was
            nx, ny = temp
            warehouse[nx, ny] = '.' 

        print(warehouse)

    return str("")

# we need a function that will check if a box is movable
# depending on the direction that it's going
def move_box(pos, dir, warehouse):
    #check to to see if there isn't anything blocking the box(s)
    potential_dir = pos + dir
    x, y = potential_dir
    if warehouse[x, y] != 'O':
        warehouse[x, y] = 'O'
    else: 
        return move_box(potential_dir, dir, warehouse)

def box_is_movable(pos, dir, warehouse):
    potential_dir = pos + dir
    x, y = potential_dir

    if warehouse[x, y] == "#":
        return False
    
    if warehouse[x, y] == ".":
        return True
    
    if warehouse[x, y] == "O":
        return box_is_movable(potential_dir, dir, warehouse)
    

