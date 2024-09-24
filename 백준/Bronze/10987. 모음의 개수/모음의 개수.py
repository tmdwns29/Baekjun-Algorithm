import sys
input = sys.stdin.readline

word = input().rstrip()
cnt = 0
for c in word:
    if c in 'aeiou':
        cnt += 1
print(cnt)