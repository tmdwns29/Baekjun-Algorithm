import sys
input = sys.stdin.readline

N,K = map(int,input().split())
coin = []
count = 0

for _ in range(N):
    coin.append(int(input()))
coin.sort(reverse=True)
for i in coin:
    if i <= K:
        count += K//i
        K -= i*(K//i)
    else:
        continue
sys.stdout.write("%d\n"%count)