import sys
input = sys.stdin.readline

N = int(input())

value1 = sum(list(range(1, N+1)))
value2 = 0

print(value1)
print(value1**2)
for i in range(1, N+1):
    value2 += i**3
print(value2)