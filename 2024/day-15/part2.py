import numpy as np
import re
import sys

np.set_printoptions(threshold=sys.maxsize, linewidth=150)

def solve(input_srt):
    map, moves = input_srt.strip().split("\n\n")
    moves = moves.replace('\n', "")
    
    # make the map into a 2d grid
    warehouse = np.array([[row for row in line] for line in map.split("\n")])

    # we need to expand the warehouse
    expanded_warehouse = []
    for row in warehouse:
        new_row = []
        for item in row:
            if item == "#":
                new_row.append("#")
                new_row.append("#")
            if item == "O":
                new_row.append("[")
                new_row.append("]")
            if item == ".":
                new_row.append(".")
                new_row.append(".")
            if item == "@":
                new_row.append("@")
                new_row.append(".")
        expanded_warehouse.append(new_row)

    expanded_warehouse = np.array(expanded_warehouse)
    
    print(expanded_warehouse)
    # hashes are walls so we can't move
    # our robot can move the boxes

    directions = {
        "<": [0, -1],
        ">": [0, 1],
        "^": [-1, 0],
        "v": [1, 0],
    } 

    # initial robot positions
    robo_position = np.argwhere(expanded_warehouse == '@')[0]
    #print(robo_position)

    for d in moves:
        move = robo_position + directions[d]

        x, y = move

        if expanded_warehouse[x, y] == ']' or expanded_warehouse[x, y] == '[' and box_is_movable(move, directions[d], expanded_warehouse):
            move_box(move, directions[d], expanded_warehouse)
            # swap 
            expanded_warehouse[x, y] = '@'
            temp = robo_position
            robo_position = move
            # we put . were the robot was
            nx, ny = temp
            expanded_warehouse[nx, ny] = '.'
        elif expanded_warehouse[x, y] == '.':
            expanded_warehouse[x, y] = '@'
            temp = robo_position
            robo_position = move
            # we put . were the robot was
            nx, ny = temp
            expanded_warehouse[nx, ny] = '.' 

        print(expanded_warehouse)

    # get all box positions
    box_positions = np.argwhere(warehouse == 'O')
    #print(box_positions)
    total = 0
    for box_pos in box_positions:
        total += 100 * box_pos[0] + box_pos[1]

    print(total)
    return str(total)

# we need a function that will check if a box is movable
# depending on the direction that it's going
def move_box(pos, dir, warehouse):
    # check to to see if there isn't anything blocking the box(s)
    potential_dir = pos + dir
    x, y = potential_dir
    second_space = potential_dir + dir
    sx, sy = second_space

    if warehouse[x, y] != ']' or warehouse[x, y] != '[':
        warehouse[x, y] = ']'
        warehouse[sx, sy] = '['
    
    else: 
        return move_box(potential_dir, dir, warehouse)

def box_is_movable(pos, dir, warehouse):
    # we need to check now if there's at least .. two dots
    potential_dir = pos + dir
    x, y = potential_dir

    if warehouse[x, y] == "#":
        return False
    
    # here we need to make an extra lookup
    if warehouse[x, y] == ".":
        return True
    
    if warehouse[x, y] == "[" or "]":
        return box_is_movable(potential_dir, dir, warehouse)
    

