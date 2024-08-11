import sys
input = sys.stdin.readline

N = int(input())
alphabet = dict()

for _ in range(N):
    pattern, BigChar = map(str, input().split())
    alphabet[BigChar] = pattern
strings = list(map(str, input().rstrip()))
S, E = map(int, input().split())
result = ''
for key in strings:
    result += alphabet[key]
print(result[S-1:E])