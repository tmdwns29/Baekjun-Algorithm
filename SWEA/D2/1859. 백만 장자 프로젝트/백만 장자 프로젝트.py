T = int(input())

for t in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    max_value, benefit = 0, 0
    for i in range(N-1, -1, -1):
        if prices[i] > max_value:
            max_value = prices[i]
        else:
            benefit += max_value - prices[i]
    print(f'#{t+1} {benefit}')