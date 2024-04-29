import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int,input().split())

tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)] # 창고
d = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)] # 6방향 1칸이동
res = 0 # 최소 경과일수
q = deque()

def BFS():
    while q:
        x, y, z = q.popleft()

        for dx, dy, dz in d:
            nx, ny, nz = x+dx, y+dy,z+dz # 6방향 한칸이동

            # 창고 크기 범위에 속하면서 익지 않은 토마토인 경우,
            if 0<=nx<H and 0<=ny<N and 0<=nz<M and tomato[nx][ny][nz] == 0:
                tomato[nx][ny][nz] = tomato[x][y][z] + 1 # 누적 경과 일수 갱신
                q.append((nx, ny, nz)) # 영향을 받아서 익은 토마토 위치 추가

for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == 1:
                q.append((h,n,m))
BFS()

for i in tomato:
    for j in i:
        for k in j:
            if k == 0: # 창고 행마다 0이 하나라도 있으면,
                print(-1) # 토마토가 모두 익지 않았으므로 -1 출력
                exit(0) # 프로그램 종료
        res = max(res, max(j)) # 창고 행을 반복 탐색해서 가장 큰 값(최소 경과일수)을 갱신

print(res-1) # 1에서 시작했으므로 1을 빼준 값이 최소 경과일수