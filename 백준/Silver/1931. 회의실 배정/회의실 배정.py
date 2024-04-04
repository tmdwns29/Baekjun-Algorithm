import sys

input = sys.stdin.readline
table = []

N = int(input())

for i in range(N):
    start, end = map(int, input().split())
    table.append((start, end))
table.sort(key=lambda x : (x[1], x[0]))        

endtime = table[0][1]
cnt = 1
for i in range(1, N):
    if table[i][0] >= endtime:
        endtime = table[i][1]
        cnt += 1
sys.stdout.write("%d\n"%cnt)