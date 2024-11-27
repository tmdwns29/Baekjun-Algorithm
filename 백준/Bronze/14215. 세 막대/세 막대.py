import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
max_length = max(a,b,c)
two_length = sum([a,b,c]) - max_length

while True:
    if max_length < two_length:
        break
    max_length -= 1
print(max_length + two_length)