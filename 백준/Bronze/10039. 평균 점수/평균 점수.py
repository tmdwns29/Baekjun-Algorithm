import sys
input = sys.stdin.readline
sum = 0
for _ in range(5):
    score = int(input())
    if score < 40:
        sum += 40
        continue
    sum += score
print(sum//5)