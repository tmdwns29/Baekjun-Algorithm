N = int(input())
cnt = 0
while N != 0:
    if N > 3 or N // 3 > 1:
        N -= 3
    else:
        N -= 1
    cnt += 1
print('CY' if cnt % 2 != 0 else 'SK')