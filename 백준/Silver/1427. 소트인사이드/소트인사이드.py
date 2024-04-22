import sys
input = sys.stdin.readline

N = list(input().rstrip())

for i in range(len(N)):
    N[i] = int(N[i])
N.sort()
N.sort(reverse=True)
for i in N:
    print(i, end='')