K,N = map(int, input().split())
num = [] # 입력받을 랜선 길이들을 저장할 리스트 초기화
for i in range(K):
    num.append(int(input()))

start = 1 # 가장 작은 숫자부터 시작하기 위해 1로 초기화
long_LAN = max(num) # 가장 긴 랜선길이 설정

while start <= long_LAN: # 이분탐색 시작, 시작길이가 가장 긴 랜선길이보다 작거나 같을 때까지 반복
    mid = (start+long_LAN)//2 # 중간 값 설정
    LAN = 0 # 랜선 개수 0으로 초기화
    for i in num: # 입력받은 길이들을,
        LAN += i//mid # 중간값으로 나눈 몫(개수) 저장
    if LAN >= N: # 필요한 랜선 개수 이상 만들 수 있으면
        start = mid + 1 #  중간값+1 부터 long_LAN까지 탐색
    else: # 필요한 랜선 개수 만큼 만들 수 없으면
        long_LAN = mid - 1 # start부터 중간값-1 까지 탐색

print(long_LAN)