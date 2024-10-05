import sys
input = sys.stdin.readline

name = list(map(str, input().rstrip().split('-')))
for i in name:
    print(i[0],end='')