from sys import stdin
N = stdin.readline()
N_num = sorted(map(int, stdin.readline().split()))
# 입력받은 N개 숫자를 정렬
m = stdin.readline()
M_num = map(int, stdin.readline().split())

def binary(value, N, start, end):
    if start > end: # 이진 탐색 끝에 결국 값이 없는 경우
        return 0
        # start=0 > end=-1 -> 왼쪽부분 끝까지 가서 결국 값이 없을 때
        # start > end=끝인덱스 -> 오른쪽부분 끝까지 가서 결국 값이 없을 떄
    m = (start+end)//2 # 이진탐색을 위한 중간값
    if value == N[m]: return 1
    elif value < N[m]: return binary(value, N, start, m-1) # 왼쪽부분 탐색
    else: return binary(value, N, m+1, end) # 오른쪽부분 탐색

for i in M_num: # 1 3 7 9 5
    start = 0 # 처음 인덱스
    end = len(N_num)-1 # 가장 끝 인덱스
    print(binary(i, N_num, start, end))