import sys
from itertools import pairwise

input = list(sys.stdin.readlines())

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

    count = 1
    while count != 0:
        print(count)
        for i, line in enumerate(pairs):
            for j, pair in enumerate(line):
                if pair not in rules:
                    shift = updates[i].pop(j + 1)
                    updates[i].insert(j, shift)
                    if i not in not_correct:
                        not_correct.append(i)
                    else:
                        count += 1
        pairs = []
        count -= 1
        for l in updates:
            pair = list(pairwise(l))
            pairs.append(pair)
    
    corrected = []
    for n in not_correct:
        corrected.append(updates[n])
    
    for i, line in enumerate(pairs):
        for j, pair in enumerate(line):
            if pair not in rules:
                shift = updates[i].pop(j + 1)
                updates[i].insert(j, shift)
                if i not in not_correct:
                    not_correct.append(i)

    sum = 0
    for update in corrected:
        middle = int((len(update) - 1)/2)
        sum += int(update[middle])
        
    print(sum)
main()