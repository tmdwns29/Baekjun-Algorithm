import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_num = list(map(int, input().split()))
prifix_sum = []

temp = 0
for i in N_num:
    temp += i
    prifix_sum.append(temp) # 5 9 12 14 15

for _ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        print(prifix_sum[j-1])
    else:
        print(prifix_sum[j-1]-prifix_sum[i-2])