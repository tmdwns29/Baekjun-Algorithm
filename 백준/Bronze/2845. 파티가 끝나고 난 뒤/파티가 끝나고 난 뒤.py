import sys
input = sys.stdin.readline

L, P = map(int, input().split())
person = list(map(int, input().split()))

print(*[p-L*P for p in person])