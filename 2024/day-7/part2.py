import numpy as np
from itertools import product

def solve(input_srt):
    lines = input_srt.strip().split("\n")
    equations = np.array([line.split(": ") for line in lines])

    count = 0

    for equation in equations:
        
        target = equation[0]
        numbers = equation[1].split(" ")
        
        value = operator_combos(target, numbers)

        if value == int(target):
            count += int(value)

    print(count)

    return str(count)

def concat(a, b):
    return int(str(a) + str(b))

def operator_combos(target, numbers):
    # if list is a b c
    # we want to check all possible combos of
    # a * b + c and a + b * c
    # but want generalize this for any sized list
    
    # Operators where using
    ops = ['+', '*', "||"]

    for combo in product(ops, repeat=len(numbers)-1):
        
        expression = str(numbers[0])

        for op, num in zip(combo, numbers[1:]):
            # concatenating strs here
            if op == "||":
                expression = f"concat({expression}, {num})"
            else: 
                expression = f"({expression} {op} {num})"
                #print(value)
        
        value = eval(expression, {'concat': concat})

        if value == int(target):
            #print(f"{expression} = {target}")
            return value
    
    return None
