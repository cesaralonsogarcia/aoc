import sys
from itertools import pairwise

input = sys.stdin.readlines()

reports = []
direction = []

def main():
    safe = 0   
    for r in input:
        report = []
        reports = r.strip().split()
        for i in range(len(reports)):
            report.append(int(reports[i]))
        notSafe = 0
        pop = 0
        if all(report[i] <= report[i + 1] for i in range(len(report) - 1)) or all(report[i] >= report[i + 1] for i in range(len(report) - 1)):
            for j in range(len(report) - 1):
                if (abs(report[j] - report[j + 1]) < 1) or (abs(report[j] - report[j + 1]) > 3):
                    notSafe += 1
                    report.pop(j + 1)
                    for k in range(len(report) - 1):
                        if abs(report[k] - report[k + 1]) > 3:
                            notSafe += 1
                            break
                    break
        else:
            notSafe += 1
            if notSafe < 1:
            #implement up or down
                for i in range(len(report) - 1):
                    if report[i] <= report[i + 1]:
                        direction.append('up')
                    else:
                        direction.append('down')
                for i in range(len(direction) - 1):
                    if direction[i] != direction[i + 1]:
                        report.pop(i + 1)
                        pop += 1
                        for j in range(len(report) - 1):
                            if (abs(report[j] - report[j + 1]) < 1) or (abs(report[j] - report[j + 1]) > 3):
                                notSafe += 1
                            break
        if notSafe < 1:
                safe += 1         
    print(safe)
    
    

main()

# def main():
#     safe = 0  
#     for r in input:
#         ascending = False
#         descending = False
#         report = []
#         direction = []
#         reports = r.strip().split()
#         for i in range(len(reports)):
#             report.append(int(reports[i]))
#         notSafe = 0
#         if all(report[i] <= report[i + 1] for i in range(len(report) - 1)):
#             ascending = True
#         elif all(report[i] >= report[i + 1] for i in range(len(report) - 1)):
#             descending = True
#         else:
#             for i in range(len(report) - 1):
#                 if report[i] <= report[i + 1]:
#                     direction.append('up')
#                 else:
#                     direction.append('down')
#             for i in range(len(direction) - 1):
#                 if direction[i] != direction[i + 1]:
#                     report.pop(i + 1)
#                     break
#             if not safeCheck(report):
#                 notSafe += 1
#             else:
#                 safe += 1 
#         if ascending or descending:
#             for j in range(len(report) - 1):
#                 if abs(report[j] - report[j + 1]) > 3:
#                     notSafe += 1
#                 elif abs(report[j] - report[j + 1]) == 0:
#                     notSafe += 1
#                     report.pop(j)
#                     if not safeCheck(report):
#                         notSafe += 1
#                     # else:
#                     #     safe += 1
#                     break
#             if notSafe == 0:
#                 safe += 1         
#     print(safe)

# def safeCheck(report):
#     for j in range(len(report) - 1):
#                     if (abs(report[j] - report[j + 1]) < 1) or (abs(report[j] - report[j + 1]) > 3):
#                         return False
#                     return True
    
# main()
