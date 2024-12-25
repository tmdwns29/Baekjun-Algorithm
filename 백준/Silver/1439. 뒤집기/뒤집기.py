import sys
input = sys.stdin.readline

S = input().rstrip()
cnt_0, cnt_1  = 0, 0

for i in range(1, len(S)):
    if S[i-1] == '0' and S[i] == '1':
        cnt_0 += 1
    elif S[i-1] == '1' and S[i] == '0':
        cnt_1 += 1
print((cnt_1+cnt_0)-min(cnt_1,cnt_0))