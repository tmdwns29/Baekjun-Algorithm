import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    temp = [int(i) for i in list(input().rstrip())]
    arr.append(temp)

def quadtree(n, arr):
    s = 0
    for l in arr:
        s += sum(l) # 영상에 있는 1의 개수 합

    if s == n**2: # 영상 전체가 1로 이루어져 있으면 1 리턴
        return '1'
    if not s:     # 영상 전체가 0으로 이뤄져 있으면 0 리턴
        return '0'
    
    # 1과 0이 섞여있는 경우
    half = n//2 # 4등분 기준 선
    temp = '('
    temp += quadtree(half, [l[:half] for l in arr[:half]]) # 왼쪽 위
    temp += quadtree(half, [l[half:] for l in arr[:half]]) # 오른쪽 위
    temp += quadtree(half, [l[:half] for l in arr[half:]]) # 왼쪽 아래
    temp += quadtree(half, [l[half:] for l in arr[half:]]) # 오른쪽 아래
    temp += ')'

    return temp

print(quadtree(N, arr))