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

# ideas: keep track of min and max in x, y directions, add an obstruction once the guard gets out
#        once you cross a path for a second time, start watching for min and max
#        keep track of direction to know which min or max to check for
# summary: identifying when a step is new outside of a loop/square 

def main():
    for y, l in enumerate(input):
        for x, c in enumerate(l):
            if c != '\n':
                puzzle[x , y] = c
    
    xPuzzle, yPuzzle = max(puzzle) # get size of puzzle
    start = list(key for key,value in puzzle.items() if value == '^') # get starting coordinate
    coordinate = start[0]
    j = 0
    walking = True
    path = [] # history for steps
    corners = [start[0]] # add first position as a corner
    allcorners = [start[0]]
    positions = 1 # counter for unique positions
    obstructions = 0 # counter for obstructions
    allcorners = []
    while walking:
        step = tuple(sum(move) for move in zip(moves[j], coordinate))
        a, b = coordinate
        if (a > 0 and a < xPuzzle) and (b > 0 and b < yPuzzle):
            if coordinate != step:
                if puzzle[step] != '#':
                    puzzle[coordinate] = 'X'
                    path.append(coordinate)
                    coordinate = step
                elif puzzle[step] == '#':
                    corners.append(coordinate)
                    allcorners.append(coordinate)
                    if len(corners) > 3:
                        # print(corners)
                        square = (corners[2][0], corners[0][1])
                        if square in allcorners:
                            square = (corners[0][0], corners[2][1])
                        if square in path:
                            obstructions += 1
                    if len(corners) == 4:
                        corners = corners[1:]
                    if j < 3:
                        j += 1
                    else:
                        j = 0
        else:
            walking = False

    if len(corners) > 2:
        square = (corners[2][0], corners[0][1])
        if square in path:
            obstructions += 1
    
    # print(corners)
    print(allcorners)      
    print(obstructions)

main()
