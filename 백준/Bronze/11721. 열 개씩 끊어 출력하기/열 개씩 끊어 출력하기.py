import sys
input = sys.stdin.readline

arr = input().rstrip()

for i,j in enumerate(arr):
    if i != 0 and i % 10 == 0:
        print()
    sys.stdout.write("%c"%j)