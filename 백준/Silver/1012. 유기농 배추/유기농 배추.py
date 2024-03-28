import sys
input = sys.stdin.readline

#    l   r  d   u
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    q = [(x, y)]
    bat[x][y] = 0

    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if bat[nx][ny]:
                q.append((nx, ny))
                bat[nx][ny] = 0

T = int(input())

for _ in range(T):
    M,N,K = map(int, input().split())
    bat = [[0]*M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        y, x = map(int, input().split())
        bat[x][y] = 1
    
    for i in range(N):
        for j in range(M):
            if bat[i][j]:
                BFS(i,j)
                cnt += 1

    print(cnt)