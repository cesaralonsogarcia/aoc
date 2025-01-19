import sys

input = list(sys.stdin.readlines())

puzzle = {}

# [[dx, dy]] = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1,], [0, -1], [1, -1]]

def main():
    print(input)
    for y, l in enumerate(input):
        for x, c in enumerate(input[y]):
            # print(f'x: {x}, y: {y} for {c}')
            puzzle[x, y] = c
            
    letterX = list(key for key, value in puzzle.items() if value == 'X')
    print(letterX)
    
main()