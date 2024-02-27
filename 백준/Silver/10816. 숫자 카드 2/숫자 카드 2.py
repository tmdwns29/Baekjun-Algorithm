import sys
input = sys.stdin.readline

N = int(input())
N_num = sorted(list(map(int,input().split())))
# -10 -10 2 3 3 6 7 10 10 10

M = int(input())
M_num = list(map(int,input().split()))

count = {} # 딕셔너리 선언
for i in N_num: # N_num에 있는 숫자들을 순회
    if i in count: # count안에 N_num에 들어있는 숫자가 있다면,
        count[i] += 1 # 중복이란 의미이므로 원래 값과 +1
    else:
        count[i] = 1 # 없으므로, 새로운 값 추가 +1
# count딕셔너리 각 인덱스에는 N_num의 숫자값을 갖는다

def binary(arr, target, start, end):
    if start > end: # 찾으려는 값이 없는 경우,
        return 0
    mid = (start+end)//2 # 중간 값
    if arr[mid] == target: # 중간 값이 찾는 값과 같으면,
        return count.get(target)
    elif arr[mid] < target: # 찾는 값이 중간 값보다 크면,
        return binary(arr, target, mid+1, end) # 오른쪽 부분 다시 탐색
    else:
        return binary(arr, target, start, mid-1) # 왼쪽 부분 다시 탐색

for target in M_num: # M_num의 값 순회
    print(binary(N_num, target, 0, len(N_num)-1), end=' ')