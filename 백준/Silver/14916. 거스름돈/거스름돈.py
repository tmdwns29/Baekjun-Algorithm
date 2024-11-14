import sys
input = sys.stdin.readline

N = int(input())
coin_cnt = 0

while N >= 0:
    if N % 5 == 0: # 5의 배수이면, 최소개수
        coin_cnt += (N // 5)
        print(coin_cnt)
        break
    N -= 2 # 3kg 차감 후,
    coin_cnt += 1 # 동전 1개 추가

else: # N이 음수면 2 or 5로 나누어 떨어지지 않음
    print(-1)