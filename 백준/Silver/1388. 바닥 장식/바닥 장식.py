import sys
input = sys.stdin.readline

N, M = map(int, input().split())
floor = []
visit = [[0]*M for _ in range(N)]
d = [[(-1,0),(1,0)],[(0,-1),(0,1)]]

def BFS(a, b):
    q = [(a,b)]
    visit[a][b] = 1
    
    while q:
        x, y = q.pop(0)
        dir, shape = 0, '|'

        if floor[x][y] == '-':
            dir, shape = 1, '-'
        
        for dx, dy in d[dir]:
            nx, ny = x+dx, y+dy

            if 0<= nx < N and 0<= ny < M and not visit[nx][ny] and floor[nx][ny] == shape:
                visit[nx][ny] = 1
                q.append((nx,ny))

for i in range(N):
    temp = list(map(str, input().rstrip()))
    floor.append(temp)

cnt = 0

for i in range(N):
    for j in range(M):
        if not visit[i][j]:
            BFS(i,j)
            cnt += 1
print(cnt)