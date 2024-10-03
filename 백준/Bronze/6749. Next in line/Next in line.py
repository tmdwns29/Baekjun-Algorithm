import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
if a > b:
    print(a+(a-b))
else:
    print(b+(b-a))