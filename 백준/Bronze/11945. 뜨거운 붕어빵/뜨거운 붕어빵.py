import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = []

for _ in range(N):
    line = input().rstrip()
    table.append(line)
for t in table:
    print(t[-1::-1])