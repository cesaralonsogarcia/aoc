import sys
from itertools import pairwise

input = list(sys.stdin.readlines())

# use '//' = float division
def main():
    rules = []
    updates = []
    pairs = []
    not_correct = []
    for l in input:
        if l != '\n':
            line = l.strip()
            if '|' in line:
                rule = tuple(line.replace('|', ' ').split())
                rules.append(rule)
            else:
                update = line.split(',')
                updates.append(update)
                pair = list(pairwise(update))
                pairs.append(pair)

    for i, line in enumerate(pairs):
        for pair in line:
            if pair not in rules:
                if i not in not_correct:
                    not_correct.insert(0, i)

    for n in not_correct:
        updates.pop(n)

    sum = 0
    for update in updates:
        middle = int((len(update) - 1)/2)
        sum += int(update[middle])

    print(sum)
main()
