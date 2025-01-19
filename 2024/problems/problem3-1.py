import sys
import re

input = sys.stdin.readlines()

def main():
    strInput = ''
    total = 0
    for l in input:
        letter = l.strip()
        strInput = strInput + letter
    equation = re.findall('mul\((\d+)\,(\d+)\)', strInput)
    strInput = ''
    for e in equation:
        total = total + int(e[0]) * int(e[1])
    print(total)
        
main()