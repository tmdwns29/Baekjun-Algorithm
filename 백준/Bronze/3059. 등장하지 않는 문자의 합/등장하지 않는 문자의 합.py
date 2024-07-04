import sys
input = sys.stdin.readline

T = int(input())
al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for _ in range(T):
    res = 0
    S = list(map(str, input().rstrip()))
    for i in range(len(al)):
        if al[i] not in S:
            res += i + 65
    print(res)