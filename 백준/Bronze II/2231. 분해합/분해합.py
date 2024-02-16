N = int(input()) # 정수 입력받기
result = 0 # 분해합 변수
for i in range(1, N+1): # 1부터 N까지 반복하며,
    nums = list(map(int, str(i))) # i값의 각 자리수를 리스트에 매핑
    result = sum(nums) + i # result = 각자리수 더한 값 + i(현재 생성자)
    if result == N: # 분해합이 N과 같으면,
        print(i) #  이 시점의 생성자 출력
        break
    if i == N: # 생성자와 N값이 같으면 생성자가 없으므로,
        print(0) # 0 출력