import sys
input = sys.stdin.readline

A = list(map(str, input().rstrip()))
B = list(map(str, input().rstrip()))
LCS = [['']*(len(B)+1) for _ in range(len(A)+1)]
result = []
for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + A[i-1]
        else:
            if len(LCS[i][j-1]) >= len(LCS[i-1][j]):
                LCS[i][j] = LCS[i][j-1]
            else:
                LCS[i][j] = LCS[i-1][j]

print(len(LCS[-1][-1]))
print(LCS[-1][-1])