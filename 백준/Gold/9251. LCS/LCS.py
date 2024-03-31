import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()
LCS = [[0]*(len(A)+1) for _ in range(len(B)+1)]

for i in range(1, len(B)+1):
    for j in range(1, len(A)+1):
        if A[j-1] == B[i-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
print(LCS[-1][-1])