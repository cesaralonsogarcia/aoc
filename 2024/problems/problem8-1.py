import sys
from collections import Counter

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

    antennas_list = list(antennas.items())

    for i, (coordinates, character) in enumerate(antennas_list):
        for j in range(i + 1, len(antennas_list)):
            next_coordinates, next_character = antennas_list[j]
            if character == next_character:
                a, b = coordinates
                c, d = next_coordinates
                x = abs(a - c)
                y = abs(b - d)
                if a < c:
                    x1 = a - x
                    x2 = c + x
                elif a > c:
                    x1 = a + x
                    x2 = c - x
                if b < d:
                    y1 = b - y
                    y2 = d + y
                elif b > d:
                    y1 = b + y
                    y2 = d - y
                if (x1 >= 0 and x1 <=xLen) and (y1 >=0 and y1 <= yLen):
                    antinodes[x1, y1] = '#'
                if (x2 >= 0 and x2 <=xLen) and (y2 >=0 and y2 <= yLen):
                    antinodes[x2, y2] = '#'

    antinode_count = Counter(antinodes.values())
    print(antinode_count)
    
main()