import sys
input = sys.stdin.readline

board = [input().rstrip() for _ in range(8)]
cnt = 0
i = 0
while i <= 7:
    if i % 2 == 0:
        cnt+=board[i][0:8:2].count('F')
    else:
        cnt+=board[i][1:8:2].count('F')
    i+=1
print(cnt)