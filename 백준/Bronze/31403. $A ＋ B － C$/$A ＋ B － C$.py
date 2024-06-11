import sys
input = sys.stdin.readline

abc = [input().rstrip() for _ in range(3)]

print(int(abc[0])+int(abc[1])-int(abc[2]))
print(int(abc[0]+abc[1])-int(abc[2]))