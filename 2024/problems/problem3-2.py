import sys
import re

input = sys.stdin.readlines()

def main():
    strInput = ''
    enabled = True
    total = 0
    indexList = []
    for l in input:
        letter = l.strip()
        strInput = strInput + letter
    equation = re.findall('(mul\((\d+)\,(\d+)\)|do\(\)|don\'t\(\))', strInput)
    for i in range(len(equation)):
        if equation[i][0] == 'do()':
            enabled = True
        elif equation[i][0] == 'don\'t()':
            enabled = False
        elif enabled:
            total = total + int(equation[i][1]) * int(equation[i][2])
    print(total)
        
main()