import sys
input = sys.stdin.readline

N,r,c = map(int, input().split())
res = 0

while N != 0:
    N -= 1

    if r < 2**N and c >= 2**N: # 2사분면
        res += (2**N) * (2**N) * 1
        c -= (2**N)
    elif r < 2**N and c < 2**N: # 1사분면
        res += (2**N) * (2**N) * 0
    elif r >= 2**N and c < 2**N : # 3사분면
        res += (2**N) * (2**N) * 2
        r -= (2**N)
    else: # 4사분면
        res += (2**N) * (2**N) * 3
        r -= 2**N
        c -= 2**N

print(res)