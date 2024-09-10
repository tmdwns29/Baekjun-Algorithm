import sys
input = sys.stdin.readline

N = int(input())
text = list()

for n in range(1, N+1):
    text.append(input().rstrip())
for n, t in enumerate(text):
    print("%d. %s"%(n+1, t))