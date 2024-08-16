import sys
input = sys.stdin.readline

N = list(reversed(input().rstrip()))
res = 0
i = 0

for n in N:
    if n == 'A':
        res += (16**i * 10)
    elif n == 'B':
        res += (16 ** i * 11)
    elif n == 'C':
        res += (16 ** i * 12)
    elif n == 'D':
        res += (16 ** i * 13)
    elif n == 'E':
        res += (16 ** i * 14)
    elif n == 'F':
        res += (16 ** i * 15)
    else:
        res += (16 ** i * int(n))
    i += 1
print(res)