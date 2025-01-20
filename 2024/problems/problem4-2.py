import sys

input = list(sys.stdin.readlines())

puzzle = {}

increments = [(-1, 1), (1, -1), (-1, -1,), (1, 1)]

def main():
    xmas = 0
    for y, l in enumerate(input):
        for x, c in enumerate(input[y]):
            if c != '\n':
                puzzle[x, y] = c
    
    for key, value in puzzle.items():
        if value == 'A':
            mCoordinates = []
            for j in range(2):
                mCoordinates.append(key[j] + increments[0][j])
            mCoordinates = tuple(mCoordinates)
            if puzzle.get(tuple(mCoordinates)) == 'M':
                sCoordinates = []
                for j in range(2):
                    sCoordinates.append(key[j] + increments[1][j])
                if puzzle.get(tuple(sCoordinates)) == 'S':
                    mCoordinates = []
                    for j in range(2):
                        mCoordinates.append(key[j] + increments[2][j])
                    if puzzle.get(tuple(mCoordinates)) == 'M':
                        sCoordinates = []
                        for j in range(2):
                            sCoordinates.append(key[j] + increments[3][j])
                        if puzzle.get(tuple(sCoordinates)) == 'S':
                            xmas += 1
                    elif puzzle.get(tuple(mCoordinates)) == 'S':
                        sCoordinates = []
                        for j in range(2):
                            sCoordinates.append(key[j] + increments[3][j])
                        if puzzle.get(tuple(sCoordinates)) == 'M':
                            xmas += 1
            elif puzzle.get(tuple(mCoordinates)) == 'S':
                mCoordinates = []
                for j in range(2):
                    mCoordinates.append(key[j] + increments[1][j])
                if puzzle.get(tuple(mCoordinates)) == 'M':
                    sCoordinates = []
                    for j in range(2):
                        sCoordinates.append(key[j] + increments[2][j])
                    if puzzle.get(tuple(sCoordinates)) == 'S':
                        mCoordinates = []
                        for j in range(2):
                            mCoordinates.append(key[j] + increments[3][j])
                        if puzzle.get(tuple(mCoordinates)) == 'M':
                            xmas += 1
                    elif puzzle.get(tuple(sCoordinates)) == 'M':
                        mCoordinates = []
                        for j in range(2):
                            mCoordinates.append(key[j] + increments[3][j])
                        if puzzle.get(tuple(mCoordinates)) == 'S':
                            xmas += 1
    print(xmas)
    
main()