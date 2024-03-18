# [Silver I] 경로 찾기 - 11403 

[문제 링크](https://www.acmicpc.net/problem/11403) 

### 성능 요약

메모리: 31120 KB, 시간: 208 ms

### 분류

플로이드–워셜, 그래프 이론, 그래프 탐색, 최단 경로

### 제출 일자

2024년 3월 18일 15:44:52

### 문제 설명

<p>가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 정점의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄부터 N개 줄에는 그래프의 인접 행렬이 주어진다. i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻이고, 0인 경우는 없다는 뜻이다. i번째 줄의 i번째 숫자는 항상 0이다.</p>

### 출력 

 <p>총 N개의 줄에 걸쳐서 문제의 정답을 인접행렬 형식으로 출력한다. 정점 i에서 j로 가는 길이가 양수인 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력해야 한다.</p>

### 풀이
~~~python
# 플로이드 워셜 알고리즘
import sys
input = sys.stdin.readline
graph = []

N = int(input())
for i in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N): # i는 반환점
    for j in range(N): # j는 시작 정점
        for k in range(N): # k는 끝 정점
            if graph[j][i] and graph[i][k]: # 양방향 모두 간선이 존재하면
                graph[j][k] = 1 # [j,k]는 경로가 존재
for i in graph:
    print(*i)
~~~
