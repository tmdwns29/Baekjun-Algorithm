import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
IOI = 'I'+('OI'*N)
S = input().rstrip()

i,cnt = 0,0
while True:
    if i > M-len(IOI):
        break
    if S[i] == 'I' and IOI == S[i:i+len(IOI)]:
        cnt += 1
    i += 1
print(cnt)