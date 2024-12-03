import re

def solve(input_srt):
    # I believe this input is one long line
    # we just need to do some regex and find
    # all instances in str of valid mul instructions
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    numbers = r"\d{1,3}"

    result = 0

    valid_muls = re.findall(pattern, input_srt)

    for mul in valid_muls:
        nums = re.findall(numbers, mul)
        x, y = nums
        result += int(x) * int(y)

    return str(result)