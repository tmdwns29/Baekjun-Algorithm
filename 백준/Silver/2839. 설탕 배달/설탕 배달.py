N = int(input())
bag = 0

while N >= 0:
    if N % 5 == 0: # 5의 배수이면, 최소개수
        bag += (N // 5)
        print(bag)
        break
    N -= 3 # 3kg 차감 후,
    bag += 1 # 가방 1개 추가

else: # N이 음수면 3 or 5로 나누어 떨어지지 않음
    print(-1)