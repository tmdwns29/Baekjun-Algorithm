N = int(input())
dp = [0] * (N + 1)  # dp[i]는 숫자 i를 1로 만드는 최소 연산 횟수
path = [0] * (N + 1)  # path[i]는 i에 도달하기 전의 숫자

for i in range(2, N + 1):
    # 기본적으로는 i-1에서 온 경우
    dp[i] = dp[i - 1] + 1
    path[i] = i - 1

    # i가 2로 나누어 떨어질 경우 최적 선택 확인
    if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
        dp[i] = dp[i // 2] + 1
        path[i] = i // 2

    # i가 3으로 나누어 떨어질 경우 최적 선택 확인
    if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
        dp[i] = dp[i // 3] + 1
        path[i] = i // 3

# 결과 출력
steps = []
current = N
while current != 0:
    steps.append(current)
    current = path[current]

print(dp[N])  # 최소 연산 횟수
print(*steps)  # 경로