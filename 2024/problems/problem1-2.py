import sys

input = sys.stdin.readlines()

left = []
right = []

def main():
    for i in input:
        l, r = i.strip().split()
        left.append(int(l))
        right.append(int(r))
    
    sum = 0
    for y in left:
        count = 0
        for x in right:
            if y == x:
                count += 1 
        sum += y * count
    print(sum)
main()