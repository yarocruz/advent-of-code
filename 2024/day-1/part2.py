def solve(input_srt):
    lines = input_srt.strip().split("\n")
    score = []

    left_list = []
    right_list = []

    for line in lines:
        # split the line by space in between
        temp = line.split("   ")
        left_list.append(int(temp[0]))
        right_list.append(int(temp[1]))

    # let's do brute force here because can't think of 
    # a way to not do double loop
    for i in range(len(left_list)):
        count = 0
        for j in range(len(right_list)):
            if right_list[j] == left_list[i]:
                count += 1
        score.append(left_list[i] * count)
    
    result = sum(score)
    return str(result)