def solve(input_srt):
    lines = input_srt.strip().split("\n")
    distances = []

    left_list = []
    right_list = []

    for line in lines:
        # split the line by space in between
        temp = line.split("   ")
        left_list.append(int(temp[0]))
        right_list.append(int(temp[1]))
    
    # sort both list in ascending order
    left_list.sort()
    right_list.sort()

    # now we calculate distances
    for i in range(len(left_list)):
        if left_list[i] > right_list[i]:
            distances.append(left_list[i] - right_list[i])
        else:
            distances.append(right_list[i] - left_list[i])
    
    result = sum(distances)
    return str(result)