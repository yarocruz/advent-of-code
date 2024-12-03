def solve(input_srt):
    lines = input_srt.strip().split("\n")
    reports = [[int(num) for num in line.split()] for line in lines]
    safe_count = 0

    for report in reports:
        if is_safe(report):
            safe_count += 1
        else:
            for i in range(len(report)):
                modified_report = report[:i] + report[i+1:]
                if is_safe(modified_report):
                    print(report)
                    break 

    return str(safe_count)


def is_safe(report):
    diffs = []
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if diff == 0:
            return False
        diffs.append(diff)
    
    if all(1 <= d <= 3 for d in diffs):
        return True
    elif all(-3 <= d <= -1 for d in diffs):
        return True
    else:
        return False
