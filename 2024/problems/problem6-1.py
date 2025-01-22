import sys

input = list(sys.stdin.readlines())

puzzle = {}
moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
# movesDict = {
#     '^': (0, -1),
#     'v': (0, 1),
#     '>': (1, 0),
#     '<': (-1, 0)
# }

# sum of two tuples:
# x = (1, 2)
# y = (3, 4)
# result = tuple(sum(pair) for pair  in zip(x, y))

def main():
    for y, l in enumerate(input):
        for x, c in enumerate(l):
            if c != '\n':
                puzzle[x , y] = c
    
    xMax, yMax = max(puzzle) # get size of puzzle
    start = list(key for key,value in puzzle.items() if value == '^') # get starting coordinate
    coordinate = start[0]
    j = 0
    walking = True
    positions = 1 # counter for unique positions
    while walking:
        step = tuple(sum(move) for move in zip(moves[j], coordinate))
        a, b = coordinate
        if (a > 0 and a < xMax) and (b > 0 and b < yMax):
            if coordinate != step:
                if puzzle[step] != '#':
                    puzzle[coordinate] = 'X'
                    coordinate = step
                elif puzzle[step] == '#':
                    # use modulus instead - to avoid hard coding
                    if j < 3:
                        j += 1
                    else:
                        j = 0
        else:
            walking = False

    for key, value in puzzle.items():
        if value == 'X':
            positions += 1
    print(positions)

main()
