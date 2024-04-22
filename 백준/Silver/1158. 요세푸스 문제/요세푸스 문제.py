import sys
input = sys.stdin.readline

N,K = map(int,input().split())
arr = [i for i in range(1, N+1)]
res = []
i = 0

while arr:
    i += K-1
    if i>= len(arr):
        i %= len(arr)
    res.append(str(arr.pop(i)))

print('<'+', '.join(res)+'>')