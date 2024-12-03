import re

def solve(input_srt):
    # this one we include the do(), don't() and mul(x,y) in the pattern
    pattern = r'do\(\)|don\'t\(\)|mul\(\d+,\d+\)'
    numbers = r"\d{1,3}"

    result = 0
    enabled = True

    tokens = re.findall(pattern, input_srt)

    # we create a queue like system base on the enable bool
    for token in tokens:
        if token == 'do()':
            enabled = True
        elif token == 'don\'t()':
            enabled = False
        elif token.startswith('mul(') and enabled:
            nums = re.findall(numbers, token)
            x, y = nums
            result += int(x) * int(y)

    return str(result)