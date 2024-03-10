import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
N_num = list(map(int, input().split()))
N_num.reverse()
arr=deque()
for i in range(N):
    if N_num[i] == 1:
        arr.appendleft(i+1)
    elif N_num[i] == 2:
        arr.insert(1, i+1)
    elif N_num[i] == 3:
        arr.append(i+1)
for i in arr:
    sys.stdout.write('%d '%i)