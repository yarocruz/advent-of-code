import numpy as np

def solve(input_srt):
    rules, print_order = input_srt.strip().split("\n\n")
    rules = [rule.split("|") for rule in rules.split("\n")]
    print_orders = [order.split(",") for order in print_order.split("\n")]

    valid_orders = []
    for update in print_orders:
        # Map page number to indices
        pos = {page: idx for idx, page in enumerate(update)}

        correct = True
        for l, r in rules:
            if l in pos and r in pos:
                if pos[l] > pos[r]:
                    correct = False
                    break
        
        if correct:
            valid_orders.append(update)

    # loop through valid orders, find the middle, assuming that each
    # update will be and odd number length
    result = 0
    for order in valid_orders:
        mid_idx = len(order) // 2
        result += int(order[mid_idx])

    return str(result)