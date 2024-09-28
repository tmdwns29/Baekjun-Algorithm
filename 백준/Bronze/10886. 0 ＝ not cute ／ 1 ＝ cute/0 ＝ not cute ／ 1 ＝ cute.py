import sys
input = sys.stdin.readline

N = int(input())
vote = []

for _ in range(N):
    vote.append(int(input()))
print('Junhee is not cute!' if vote.count(0) > N//2 else 'Junhee is cute!')