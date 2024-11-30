def solve(input_srt):
    lines = input_srt.strip().split("\n")
    c_values = []

    for line in lines:
        first_digit = ""
        last_digit = ""

        #Find first number
        for char in line:
            if char.isdigit():
                first_digit = char
                break

        #find last number
        for char in reversed(line):
            if char.isdigit():
                last_digit = char
                break

        if first_digit and last_digit:
            digits = first_digit + last_digit
            c_values.append(int(digits))
    
    result = sum(c_values)
    return str(result)