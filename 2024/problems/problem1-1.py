import sys

input = sys.stdin.readlines()

left = []
right = []

def main():
    for i in input:
        # n = i.strip()
        # l, r = n.split()
        l, r = i.strip().split()
        left.append(int(l))
        right.append(int(r))
    left.sort()
    right.sort()
    
    sum = 0
    for x in range(len(input)):
        sum += abs(left[x] - right[x])
    print(sum)
main()