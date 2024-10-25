import sys
input = sys.stdin.readline

def BFS(n):
    q = []
    q.append(n)

    while q:
        c = q.pop(0)

        for num in lst[c]:
            if not visit[num]:
                q.append(num)
                visit[num] = visit[c]+1
n = int(input())
m = int(input())

lst = [[]for _ in range(n+1)]
visit = [0] * (n+1)
cnt = 0

for _ in range(m):
    a,b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
BFS(1)
for i in visit[2:]:
    if 0 < i <= 2:
        cnt+=1
print(cnt)