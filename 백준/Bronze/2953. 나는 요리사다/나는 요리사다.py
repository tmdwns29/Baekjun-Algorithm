import sys
input = sys.stdin.readline

winner = 0
max_score = 0
for i in range(1, 6):
    a,b,c,d = map(int, input().split())
    score = a+b+c+d
    if max_score < score:
        max_score = score
        winner = i
print(winner, max_score)