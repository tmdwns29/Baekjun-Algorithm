import sys
input = sys.stdin.readline

S = int(input())
F = int(input())

print('high speed rail' if S <= F else 'flight')