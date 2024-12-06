import sys

def read_input():
    with open("input.txt", "r") as file:
        return file.read()
    
if __name__ == "__main__":
    input_data = read_input()

    if len(sys.argv) < 2:
        print("Usage: Python main.py [part1|part2]")
        sys.exit(1)

    part = sys.argv[1]

    if part == "part1":
        from part1 import solve
    elif part == "part2":
        from part2 import solve
    else:
        print("Invalid argument. Use 'part1' or 'part2'.")
        sys.exit(1)

    result = solve(input_data)
    print(f"Result for {part}: {result}")        