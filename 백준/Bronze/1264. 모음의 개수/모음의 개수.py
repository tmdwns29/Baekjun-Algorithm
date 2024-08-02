import sys
input = sys.stdin.readline

while True:
    cnt = 0
    word = input().rstrip()
    if word == '#': break
    for i in word:
        if i in 'AaEeIiOoUu':
            cnt += 1
    print(cnt)