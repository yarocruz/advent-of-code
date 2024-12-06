import numpy as np

def solve(input_srt):
    rules, print_order = input_srt.strip().split("\n\n")
    rules = [rule.split("|") for rule in rules.split("\n")]
    print_orders = [order.split(",") for order in print_order.split("\n")]

    invalid_orders = []
    for update in print_orders:
        # Map page number to indices
        pos = {page: idx for idx, page in enumerate(update)}

        correct = False
        for l, r in rules:
            if l in pos and r in pos:
                if pos[l] > pos[r]:
                    correct = True
                    break
        
        if correct:
            invalid_orders.append(update)

    # fix the invalid orders
    for update in invalid_orders:
        # Map page number to indices
        pos = {page: idx for idx, page in enumerate(update)}

        print(pos)

        for l, r in rules:
            if l in pos and r in pos:
                if pos[l] > pos[r]:
                    # flippy floppy
                    temp = update[pos[l]]
                    update[pos[l]] = update[pos[r]]
                    update[pos[r]] = temp
                elif pos[r] > pos[l]:
                    temp = update[pos[r]]
                    update[pos[r]] = update[pos[l]]
                    update[pos[l]] = temp

    
    # loop through valid orders, find the middle, assuming that each
    # update will be and odd number length
    result = 0
    for order in invalid_orders:
        mid_idx = len(order) // 2
        result += int(order[mid_idx])

    return str(result)