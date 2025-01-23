import sys
from itertools import product

input = list(sys.stdin.readlines())

operators = ['+', '*']

def main():
    calibration = 0
    for l in input:
        l = l.split()
        line = []
        operation = []
        possibilities = []
        total = []
        for e in l:
            number = e.strip(':')
            line.append(number)
        result = int(line.pop(0))
        possibilities = list(product(operators, repeat=len(line)-1))
        if len(possibilities) == 2:
            possibilities = operators
        for equation in possibilities:
            calculation = int(line[0])
            for i in range(len(equation)):
                if equation[i] == '+':
                    calculation += int(line[i + 1])
                else:
                    calculation = calculation * int(line[i + 1])
            if calculation == result:
                if calculation in total:
                    break
                else:
                    total.append(calculation)
                    print(f'calculation: {calculation} result: {result}')
                    calibration += calculation
    print(calibration)

main()

