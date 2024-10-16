import sys
input = sys.stdin.readline

while True:
    N = int(input())
    sum_ = 0

    if N == 0: break
    for i in range(1, N+1):
        sum_ += i
    print(sum_)