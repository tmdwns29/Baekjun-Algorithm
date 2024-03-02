N = int(input())
arr = []
for i in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

for i in arr:
    rank = 1
    for j in arr: # 비교 대상
        if i[0] < j[0] and i[1] < j[1]: # 덩치가 "큰" 경우
            rank += 1 # 순위 1 밀림
    print(rank, end=' ')