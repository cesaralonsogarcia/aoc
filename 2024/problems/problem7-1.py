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
        for e in l:
            number = e.strip(':')
            line.append(number)
        result = int(line.pop(0))
        print(f'result: {result}')
        possibilities = list(product(operators, repeat=len(line)-1))
        # print(line)
        # print(possibilities, len(possibilities))
        if len(possibilities) == 2:
            possibilities = operators
        # print(possibilities)
        for equation in possibilities:
            calculation = ''
            for i in range(len(equation)):
                # print(line[i], equation[i])
                calculation += line[i] + equation[i]
            calculation += line[i + 1]
            total = eval(calculation)
            if total == result:
                print(f'total: {total} result: {result}')
                calibration += total
    print(calibration)
    print(len(input))
        # for i in range(1):
        #     for p in possibilities:
        #         for sign in p:
        #             print(sign)
        #             total = line[0]
        #             for n in range(1, len(line)):
        #                 print(line[n])
        #                 print(f'p: {p}')
        #                 if '+' in sign:
        #                     total += line[n]
        #                 if '*' in sign:
        #                     total = total * line[n]
        #             print(f'total: {total}')       

                    
        # print(possibilities)
        # for i in range(possibilities):
        #     for element in range(1, len(line)):
        #         equation =
    
    
    
    # total = number[0]
    # for number in numbers: maybe use index
    # for sign in signs:
    # if sign == '+'
    # total += next(number)
    # if sign == '*'
    # total = total * next(number)
    # check if total against result

main()

