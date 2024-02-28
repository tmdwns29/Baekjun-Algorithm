import sys
input = sys.stdin.readline

N, K = map(int, input().split())

i = 0
queue = [i for i in range(1, N+1)]
arr = []

while queue:
    i += K-1
    if i >= len(queue):
        i %= len(queue)
    arr.append(str(queue.pop(i)))

print('<'+', '.join(arr)+'>')