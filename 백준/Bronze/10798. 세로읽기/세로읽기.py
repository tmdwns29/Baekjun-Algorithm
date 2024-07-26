import sys
input = sys.stdin.readline

text = []
max_len = 0

for i in range(5):
    text.append(list(map(str, input().rstrip())))
    if max_len < len(text[i]):
        max_len = len(text[i])

for i in range(5):
    if max_len > len(text[i]):
        for _ in range(max_len-len(text[i])):
            text[i].append('')

for i in range(len(text[0])):
    for j in range(5):
        if text[j][i] == '':
            continue
        print(text[j][i], end='')