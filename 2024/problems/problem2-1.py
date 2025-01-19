import sys

input = sys.stdin.readlines()

reports = []

def main():
    safe = 0   
    for r in input:
        report = []
        reports = r.strip().split()
        for i in range(len(reports)):
            report.append(int(reports[i]))
        notSafe = 0
        if all(report[i] <= report[i + 1] for i in range(len(report) - 1)) or all(report[i] >= report[i + 1] for i in range(len(report) - 1)):
            for j in range(len(report) - 1):
                if (abs(report[j] - report[j + 1]) < 1) or (abs(report[j] - report[j + 1]) > 3):
                    notSafe += 1
            if notSafe == 0:
                safe += 1     
    print(safe)
    
main()
