import sys
input = sys.stdin.readline

while True:
    N = int(input())
    word = []
    if N == 0: break
    for i in range(N):
        tmp1 = input().rstrip()
        tmp2 = tmp1.lower()
        word.append((tmp1, tmp2))
    word.sort(key=lambda x: x[1])
    print(word[0][0])