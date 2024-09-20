import sys
input = sys.stdin.readline

while True:
    ciper_text = input().rstrip()
    if ciper_text == 'END': break
    print(''.join(list(reversed(ciper_text))))