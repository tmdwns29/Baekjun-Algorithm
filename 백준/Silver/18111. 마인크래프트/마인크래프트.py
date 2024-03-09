import sys
input = sys.stdin.readline

N,M,B = map(int, input().split())
arr=[]
for _ in range(N):
    arr.extend(map(int, input().split()))

time = [0 for _ in range(257)] # 256개의 0 리스트로 저장
height = 0 # 땅의 높이
for g in range(257): # g = 현재의 땅 높이
    block = B # 인벤토리 블록 개수
    for i in arr: # 땅의 높이 순회
        if i <= g: # 집터가 현재 땅 높이보다 낮으면
            time[g] += g - i # 개당 소요시간 1초
            block -= g - i # 블록을 빼서 채워줌
        else: # 집터가 현재 땅 높이보다 높으면
            time[g] += 2 * (i - g) # 개당 소요시간 2초
            block += i - g # 높으만큼 블록을 빼서 인벤토리에 채움
    if block >= 0 and time[g] <= time[height]:
        # 인벤토리에 블록이 남아있고, 현재 땅높이에서 소요시간이 height에서의 소요시간보다 짧거나 같으면
        height = g # height값을 현재 땅 높이로 업데이트

print(time[height], height)