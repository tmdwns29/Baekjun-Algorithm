import sys
input = sys.stdin.readline

N = int(input())
container = []
result = 0

for _ in range(N):
    L, H = map(int, input().split())
    container.append((L,H))

container.sort()

i = 0
for c in container:
    if c[1] > result:
        result = c[1]
        idx = i
    i += 1

h = container[0][1]

for i in range(idx):
    if h < container[i+1][1]:
        result += h*(container[i+1][0]-container[i][0])
        h = container[i+1][1]
    else:
        result += h*(container[i+1][0]-container[i][0])

h = container[-1][1]

for i in range(N-1, idx, -1):
    if h < container[i-1][1]:
        result += h*(container[i][0]-container[i-1][0])
        h = container[i-1][1]
    else:
        result += h*(container[i][0]-container[i-1][0])

print(result)