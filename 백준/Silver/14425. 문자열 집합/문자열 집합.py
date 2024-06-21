import sys
input = sys.stdin.readline

N,M = map(int, input().split())
string = []
cnt = 0

for _ in range(N):
    string.append(input().rstrip())
for _ in range(M):
    temp = input().rstrip()
    if temp in string:
        cnt+=1

print(cnt)