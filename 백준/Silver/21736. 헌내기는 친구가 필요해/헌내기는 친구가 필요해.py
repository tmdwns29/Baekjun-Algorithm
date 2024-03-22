from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
campus, temp = [], []
start=()

for i in range(N):
    temp = list(input().rstrip())
    for j in range(M): # 시작점 I 찾기
        if temp[j] == 'I':
            start = (i, j)
            break
    campus.append(temp)

    # down  right    up     left
d = [(1,0), (0,1), (-1,0), (0,-1)]
v = [[0]*M for _ in range(N)]
p = 0

queue = deque([start])
v[start[0]][start[1]] = 1 # 시작점 I 방문 표시
while(queue):
    x, y = queue.popleft()

    for dx, dy in d:
        nx, ny = x+dx, y+dy # 1칸 이동

        # 이동한 곳이 캠퍼스를 벗어나지 않고,
        if 0<=nx<N and 0<=ny<M:
            # 벽(X)이 아니고, 방문하지 않은 곳이면 방문
            if campus[nx][ny] != 'X' and not v[nx][ny]:
                queue.append((nx,ny))
                v[nx][ny] = 1

                # 사람을 만났으면 +1
                if campus[nx][ny] == 'P':
                    p += 1
print(p if p>0 else 'TT')