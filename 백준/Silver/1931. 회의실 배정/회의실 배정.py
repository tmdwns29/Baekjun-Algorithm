import sys
input = sys.stdin.readline

N = int(input())
table = []

for _ in range(N):
    s, e = map(int, input().split())
    table.append((s, e))

table.sort(key=lambda x: (x[1],x[0]))

result = [table.pop(0)]
for i in table:
    if result[-1][1] <= i[0]:
        result.append(i)
print(len(result))