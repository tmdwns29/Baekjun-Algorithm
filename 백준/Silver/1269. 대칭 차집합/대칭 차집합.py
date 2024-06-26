import sys
input = sys.stdin.readline

A,B = map(int, input().split())
Aset = set(map(int, input().split()))
Bset = set(map(int, input().split()))

print(len(Aset.difference(Bset))+len(Bset.difference(Aset)))