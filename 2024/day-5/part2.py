import numpy as np

def topological_sort(nodes, edges):
    """
    Perform a topological sort on the given graph.
    nodes: a set of node identifiers
    edges: a dict of node -> list of nodes that must follow it
    Return a list of nodes in a valid topological order.
    """
    # Compute in-degrees
    in_degree = {node: 0 for node in nodes}
    for node in edges:
        for nxt in edges[node]:
            in_degree[nxt] += 1

    # Find all nodes with zero in-degree
    queue = [n for n in nodes if in_degree[n] == 0]

    sorted_list = []
    while queue:
        # Pop a node with zero in-degree
        current = queue.pop()
        sorted_list.append(current)
        # Decrease in-degree of successors
        for nxt in edges.get(current, []):
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    if len(sorted_list) != len(nodes):
        # This means there's a cycle or something went wrong.
        # But the puzzle input should be consistent.
        raise ValueError("No valid topological ordering found. The rules may have cycles.")
    return sorted_list

def solve(input_srt):
    rules, print_order = input_srt.strip().split("\n\n")
    rules = [rule.split("|") for rule in rules.split("\n")]
    print_orders = [order.split(",") for order in print_order.split("\n")]

    invalid_orders = []
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
        else:
            invalid_orders.append(update)

    # fix the invalid orders
    fixed_invalid_orders = []
    for update in invalid_orders:
        # filter rules for this update
        pages_in_update = set(update)
        filtered_rules = [(l, r) for (l, r) in rules if l in pages_in_update and r in pages_in_update]

        # build graph
        edges = {}
        for page in pages_in_update:
            edges[page] = []

        for l, r in filtered_rules:
            edges[l].append(r)

        #Topological sort the pages 
        correct_order = topological_sort(pages_in_update, edges)
        print("Correct", correct_order)
        fixed_invalid_orders.append(correct_order)
    
    # loop through valid orders, find the middle, assuming that each
    # update will be and odd number length
    result = 0
    for order in fixed_invalid_orders:
        mid_idx = len(order) // 2
        result += int(order[mid_idx])

    return str(result)