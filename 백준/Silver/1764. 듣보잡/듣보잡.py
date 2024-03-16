import sys
input = sys.stdin.readline

N,M = map(int, input().split())
deut,bo = set(), set()

for _ in range(N):
    deut.add(input().rstrip())
for _ in range(M):
    bo.add(input().rstrip())

result = sorted(list(deut & bo)) # 교집합 구하기(&)

print(len(result))
for i in result:
    print(i)