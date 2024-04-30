import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
IOI = 'I'+('OI'*N)
S = input().rstrip()

i,cnt,res = 0,0,0
while i < M:
    if S[i:i+3] == 'IOI':
        i += 2
        cnt += 1
        if cnt == N:
            cnt -= 1
            res += 1
    else:
        cnt = 0
        i += 1
print(res)