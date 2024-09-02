# 입력받기
N = int(input())  # 물건의 개수
profits = list(map(int, input().split()))  # 각 물건의 이익
prices = list(map(int, input().split()))  # 각 물건의 가격

# 전체 이익 중 가장 큰 값과 두 번째로 큰 값을 계산
max_profit = max(profits)  # 최대 이익

# 두 번째로 큰 값을 계산 (자신이 최대 이익인 경우를 처리하기 위해)
if profits.count(max_profit) > 1:
    second_max_profit = max_profit
else:
    second_max_profit = max(x for x in profits if x != max_profit)

# 각 물건의 순수익 계산
result = []
for i in range(N):
    # 자신의 기회비용 계산
    if profits[i] == max_profit:
        opportunity_cost = second_max_profit - prices[i]
    else:
        opportunity_cost = max_profit - prices[i]
    
    # 자신의 순수익 계산
    net_profit = profits[i] - opportunity_cost - prices[i]
    result.append(net_profit)

# 결과 출력
print(" ".join(map(str, result)))
