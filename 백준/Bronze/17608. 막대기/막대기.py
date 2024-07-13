import sys
input = sys.stdin.readline

N = int(input())
sticks, cnt = [], 1
for _ in range(N):
    sticks.append(int(input()))

i = len(sticks)-2
max_h = sticks[-1]
while i >= 0:
    if sticks[i] > max_h:
        max_h = sticks[i]
        cnt += 1
    i -= 1
print(cnt)