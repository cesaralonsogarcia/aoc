import sys
from itertools import product

input = list(sys.stdin.readlines())

operators = ['+', '*']

def main():
    # for l in input:
    #     l = l.split()
    #     line = []
    #     total = 0
    #     possibilites = 0
    #     for e in l:
    #         number = e.strip(':')
    #         line.append(number)
    #     result = line.pop(0)
    #     possibilities = 2 ** (len(line) - 2)
    #     for i in range(possibilities):
    #         for p in range(len(operators)):
    #             new_equation = ''
    #             for e in line:
    #                 new_equation += e + operators[p]
    #             print(new_equation)
                    
                    
        # print(possibilities)
        # for i in range(possibilities):
        #     for element in range(1, len(line)):
        #         equation =
    
    operation = generate_combinations(5, operators)
    
    operation2 = product(operators, repeat=5)
    print(operation)
    print(list(operation2))
    
    # total = number[0]
    # for number in numbers: maybe use index
    # for sign in signs:
    # if sign == '+'
    # total += next(number)
    # if sign == '*'
    # total = total * next(number)
    # check if total against result

def generate_combinations(length, values):
    return [''.join(e) for e in product(values, repeat=length)]
   
main()

