import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    cnt = 0
    for num in list(range(N, M+1)):
        cnt += str(num).count('0')
    print(cnt)