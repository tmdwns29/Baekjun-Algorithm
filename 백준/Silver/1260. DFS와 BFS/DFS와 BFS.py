import sys
input = sys.stdin.readline

def dfs(c):
    ans_dfs.append(c) # 방문 노드 추가
    visit[c] = 1 # 방문 표시

    for n in adj[c]:
        if not visit[n]: # 방문하지 않은 노드인 경우
            dfs(n)

def bfs(s):
    q = [] # 필요한 q, v[], 변수 생성
    q.append(s) # q에 초기 데이터 삽입

    ans_bfs.append(s) # 방문 노드 추가
    visit[s] = 1 # 방문 표시

    while q:
        c = q.pop(0)
        for n in adj[c]:
            if not visit[n]: # 0 거짓, 1 참
                q.append(n)
                ans_bfs.append(n)
                visit[n] = 1

N,M,V = map(int, input().split())
adj = [[]for _ in range(N+1)]

for _ in range(M):
    s,e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s) # 양방향

# 오름차순 정렬
for i in range(1, N+1):
    adj[i].sort()

visit = [0]*(N+1)
ans_dfs = []
dfs(V)

visit = [0]*(N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)