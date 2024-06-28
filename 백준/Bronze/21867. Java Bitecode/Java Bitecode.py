import collections
import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()

S = S.replace('J','')
S = S.replace('A','')
S = S.replace('V','')

if len(S) == 0:
    print('nojava')
else:
    print(S)