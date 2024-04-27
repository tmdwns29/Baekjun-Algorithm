import sys
input = sys.stdin.readline

d = [(-1,0),(1,0),(0,-1),(0,1)]

def BFS(a, b):
    q = [(a,b)]
    if visit[a][b]:
        return 0
    visit[a][b] = 1

    while q:
        x, y = q.pop(0)
        for dx, dy in d:
            nx, ny = x+dx, y+dy

            if 0<=nx<N and 0<=ny<N and not visit[nx][ny]:

                if RGB[x][y] == RGB[nx][ny]:
                    visit[nx][ny] = 1
                    q.append((nx, ny))

N = int(input())
RGB = [[] for _ in range(N)]
visit = [[0]*N for _ in range(N)]
cnt = 0

for i in range(N):
    temp = input().rstrip()
    for j in temp:
        RGB[i].append(j)

for i in range(N):
     for j in range(N):
         if BFS(i,j) != 0:
             cnt+=1
sys.stdout.write("%d "%cnt)

cnt=0
visit = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if RGB[i][j] == 'G':
            RGB[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if BFS(i,j) != 0:
            cnt += 1
sys.stdout.write("%d\n"%cnt)