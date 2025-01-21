import sys

input = list(sys.stdin.readlines())

puzzle = {}
moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
# moves = {
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
    
    start = list(key for key,value in puzzle.items() if value == '^')
    coordinate = start[0]

    j = 0
    print(puzzle[4, 0])
    for i in range(len(puzzle)):
        print(coordinate, puzzle[coordinate])
        step = tuple(sum(move) for move in zip(moves[j], coordinate))
        if puzzle[coordinate] != '#':
            coordinate = step
        elif puzzle[coordinate] == '#':
            if j < 3:
                j += 1
            else:
                j = 0

    print(coordinate)

main()
