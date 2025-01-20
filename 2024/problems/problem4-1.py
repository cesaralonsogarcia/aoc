import sys

input = list(sys.stdin.readlines())

puzzle = {}

increments = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1,), (0, -1), (1, -1)]

def main():
    xmas = 0
    for y, l in enumerate(input):
        for x, c in enumerate(input[y]):
            if c != '\n':
                puzzle[x, y] = c
    
    for key, value in puzzle.items():
        if value == 'X':
            for i in range(8):
                mCoordinates = []
                for j in range(2):
                    mCoordinates.append(key[j] + increments[i][j])
                mCoordinates = tuple(mCoordinates)
                if puzzle.get(tuple(mCoordinates)) == 'M':
                    aCoordinates = []
                    for j in range(2):
                        aCoordinates.append(mCoordinates[j] + increments[i][j])
                    if puzzle.get(tuple(aCoordinates)) == 'A':
                        sCoordinates = []
                        for j in range(2):
                            sCoordinates.append(aCoordinates[j] + increments[i][j])
                        if puzzle.get(tuple(sCoordinates)) == 'S':
                            xmas += 1
    print(xmas)
    
main()