import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num_list = []
for n in range(1, K+1):
    num = str(N * n)
    num_list.append(int(num[-1::-1]))
print(max(num_list))