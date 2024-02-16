N, M = map(int, input().split()) # 카드개수 N, 한도 M 입력
num = list(map(int, input().split())) # N개만큼 카드 수 입력
result = 0 # 가장 큰 3개의 수 합
for i in range(N): # 인덱스 i 0~(N-1)
    for j in range(i+1, N): # 인덱스 j (i+1)~(N-1)
        for k in range(j+1, N): # 인덱스 k (j+1)~(N-1)
            if M < num[i]+num[j]+num[k]: # 3개의 수 합이 M보다 크면,
                continue # M보다 작은 합 찾기위해 계속 반복
            else: # 3개의 수 합이 M보다 같거나 작으면,
                result = max(result, num[i]+num[j]+num[k]) # 이전 합계와 현재 합계 중 큰 수를 result에 갱신 

print(result) # 3개의 합이 M에 가장 근접한 수 출력