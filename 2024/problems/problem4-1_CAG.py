import sys
import re

input = list(sys.stdin.readlines())

puzzle = []
rows = []
columns = []
letters = []

def main():
    row = ''
    column = ''
    line = []
    preDiagonal = []
    transpose = []
    transDiagonal = []
    diagonal = []
    instances = 0
    for i in input:
        puzzle = i.strip()
        rows.append(puzzle)
    letters = list(map(list, zip(*rows)))
    for l in letters:
        for i in l:
            column = column + str(i)
        columns.append(column)
        column = ''  
    for r in rows:
        instanceRows = re.findall('(XMAS)', r)
        instanceRowsReverse = re.findall('(SAMX)', r)
        instances += len(instanceRows)  + len(instanceRowsReverse)
    for c in columns:
        instanceColumns = re.findall('(XMAS)', c)
        instanceColumnsReverse = re.findall('(SAMX)', c)
        instances += len(instanceColumns) + len(instanceColumnsReverse)
    for i in range(len(rows)):
        k = 0
        for j in range((len(rows[0]) * 3) - 1):
            if j < len(rows[0]) - 1:
                line.append(' ')
            elif j >= len(rows[0]) and j < (len(rows[0] * 2)):
                line.append(letters[i][k])
                k += 1
            else:
                line.append(' ')
        print(line)
        transDiagonal.append(line)
        line = []
    j = 1
    for i in range(len(transDiagonal)):
        preDiagonal = transDiagonal[i][j:]
        j += 1
        transpose.append(preDiagonal)
    diagonal = list(map(list, zip(*transpose)))
    preDiagonal = []
    for l in diagonal:
        for i in range(len(diagonal[0])):
            row = row + str(l[i].strip())
        preDiagonal.append(row)
        row = ''
    for p in preDiagonal:
        instanceDiagR = re.findall('(XMAS)', p)
        instanceDiagRReverse = re.findall('(SAMX)', p)
        instances += len(instanceDiagR) + len(instanceDiagRReverse)
# Reverse
    row = ''
    column = ''
    line = []
    preDiagonal = []
    transpose = []
    diagonal = []
    j = len(rows[0])
    for i in range(len(transDiagonal)):
        preDiagonal = transDiagonal[i][j:]
        j -= 1
        while len(preDiagonal) > len(rows[0] * 2) - 1:
            preDiagonal.pop()
        transpose.append(preDiagonal)
    diagonal = list(map(list, zip(*transpose)))
    preDiagonal = []
    for l in diagonal:
        for i in range(len(diagonal[0])):
            row = row + str(l[i].strip())
        preDiagonal.append(row)
        row = ''
    for p in preDiagonal:
        instanceDiagL = re.findall('(XMAS)', p)
        instanceDiagLReverse = re.findall('(SAMX)', p)
        instances += len(instanceDiagL) + len(instanceDiagLReverse)
    print(instances)       
    
main()
