import sys
input = sys.stdin.readline

N, M = map(int, input().split())
website, search = dict(), []
for i in range(N):
    address, pwd = map(str, input().rstrip().split())
    website[address] = pwd
for i in range(M):
    search.append(input().rstrip())
for i in search:
    sys.stdout.write('%s\n'%website[i])