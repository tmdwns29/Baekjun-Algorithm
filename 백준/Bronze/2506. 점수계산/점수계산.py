import sys
input = sys.stdin.readline

N = int(input())
results = list(map(int, input().split()))
combo = 0
score = 0

for result in results:
    if result == 1:
        combo += 1
        score += combo
    else:
        combo = 0
print(score)