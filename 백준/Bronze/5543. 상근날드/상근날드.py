import sys
input = sys.stdin.readline

hmbgr = []
for _ in range(3):
    hmbgr.append(int(input()))
coke = int(input())
cidar = int(input())
print(min(hmbgr)-50 + int(coke if coke < cidar else cidar))