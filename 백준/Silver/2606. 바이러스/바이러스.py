import sys
input = sys.stdin.readline

com = int(input())
line = int(input())
line_arr = [[] for _ in range(com+1)]
bfs_res = []
v = [0]*(com+1)

def BFS(N):
    q=[]
    q.append(N)

    bfs_res.append(N)
    v[N] = 1

    while q:
        N = q.pop(0)
        for n in line_arr[N]:
            if not v[n]:
                q.append(n)
                bfs_res.append(n)
                v[n] = 1

for _ in range(line):
    a,b = map(int, input().split())
    line_arr[a].append(b)
    line_arr[b].append(a)

BFS(1)

print(len(bfs_res)-1)