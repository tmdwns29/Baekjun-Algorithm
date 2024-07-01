from itertools import permutations
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    L = list(map(str, input().rstrip()))
    P = permutations(L, len(L))
    print("Case # %d:"%(i+1))
    for res in P:
        print(''.join(res))