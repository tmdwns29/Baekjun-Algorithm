import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

num,j = [], 1
for i in P:
    num.append((j,i))
    j+=1
num.sort(key=lambda x: x[1])
Pi,res = 0,0

for i in num:
    Pi += i[1]
    res += Pi
sys.stdout.write("%d"%res)