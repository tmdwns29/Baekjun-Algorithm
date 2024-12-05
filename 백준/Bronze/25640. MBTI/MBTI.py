import sys
input = sys.stdin.readline

jinho = input().rstrip()

N = int(input())
cnt = 0
for _ in range(N):
    friends = input().rstrip()
    if jinho == friends:
        cnt += 1
print(cnt)