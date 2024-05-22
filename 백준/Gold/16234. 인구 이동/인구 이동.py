from collections import deque
import sys
input = sys.stdin.readline

def BFS(a,b):
    q = deque([(a,b)])
    union = [] # 연합 리스트
    union.append((a,b)) # 연합에 나라 추가

    while q:
        x,y = q.popleft()
        
        for dx, dy in d:
            nx,ny = x+dx, y+dy # 탐색할 나라에서 인접한 나라

            if 0<=nx<N and 0<=ny<N and not visit[nx][ny]: # 다음나라가 탐색되지 않았으면,
                if L<=abs(area[x][y]-area[nx][ny])<=R: # L <= 두 나라의 인구 차 <= R 성립하면
                    visit[nx][ny] = 1 # 방문 표시
                    q.append((nx,ny)) # 다음 나라 탐색리스트에 추가
                    union.append((nx,ny)) # 연합에 나라 추가
    if len(union)<=1: # 연합에 속한 나라 개수가 1개 이하면(연합이 형성되지 않았으면)
        return 0
    result = sum(area[x][y] for x,y in union)//len(union) # (연합에 속한 나라의 인구합)//(나라 수) = 평균 인구수
    for x,y in union: # 계산한 평균 인구수를 연합에 속한 나라에 갱신
        area[x][y] = result
    return 1 # 인구이동 완료

N,L,R = map(int, input().split()) # 4 10 50
area = [list(map(int, input().split())) for _ in range(N)]
d = [(-1,0),(1,0),(0,-1),(0,1)]
day = 0

while True: # 한번 반복 == 하루 경과
    stop = 0 # 종료조건 변수
    visit = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visit[i][j]: # 탐색하지 않은 나라일 경우,
                visit[i][j] = 1
                stop += BFS(i, j) # 연합형성과 인구이동까지 마쳤으면(1), 그렇지 않으면(0) 리턴값을 stop에 저장
    if not stop: # 연합형성, 인구이동이 이루어지지 않았을 때, 종료
        break
    day += 1

print(day)