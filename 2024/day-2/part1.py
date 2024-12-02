def solve(input_srt):
    lines = input_srt.strip().split("\n")
    
    reports = []
    unsafe_count = 0
    
    for line in lines:
        report = line.split(" ")
        reports.append(report)

    for report in reports:
        decreasing = is_valid_decrease(int(report[0]), int(report[1]))
        increasing = is_valid_increase(int(report[0]), int(report[1]))
        
        for i in range(1, len(report)):
            if increasing == True and i < len(report) - 1:
                if not is_valid_increase(int(report[i]), int(report[i+1])):
                    unsafe_count += 1
                    break
            if decreasing == True and i < len(report) - 1:
                if not is_valid_decrease(int(report[i]), int(report[i+1])):
                    unsafe_count += 1
                    break
            if not decreasing and not increasing:
                print("Nothing increased nor decreased")
                unsafe_count += 1
                break

    print(len(reports), unsafe_count)       

    return str(len(reports) - unsafe_count)

def is_valid_increase(curr, next):
    if next - curr > 0 and next - curr <= 3:
        return True
    return False

def is_valid_decrease(curr, next):
    if curr - next > 0 and curr - next <= 3:
        return True
    return False