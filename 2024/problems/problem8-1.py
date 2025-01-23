import sys

input = list(sys.stdin.readlines())

puzzleMap = {}

def main():
    characters = []
    antennas = {}
    for y, l in enumerate(input):
        for x, c in enumerate(l):
            if c != '\n':
                puzzleMap[x, y] = c # store every coordinate
    
    antinodes = puzzleMap # create copy to store locations of antinodes
    xLen, yLen = max(puzzleMap) # get size of map
    
    for coordinates, antenna in puzzleMap.items():
        if antenna != '.' :
            antennas[coordinates] = antenna # get location for all antennas
        # if antenna[0] == antenna[1]:
        #   subtract the coordinates
        #   store location 1 and location 2 of antennas to determine antinode locations
        #   add antinode at subtraction by changing location to #
    print(antennas)
    
main()