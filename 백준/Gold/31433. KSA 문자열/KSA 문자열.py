X = input()
answer = 10000000
KSA = ['K', 'S', 'A']

def calc(string, cnt):
    idx = 0
    for char in string:
        if char == KSA[idx % 3]:  # 일치
            idx += 1
        else:  # 일치하지 않으니 제거
            cnt += 1
    cnt += abs(idx - len(X))
    global answer
    answer = min(answer, cnt)

calc(X, 0)
calc('K' + X, 1)
calc('KS' + X, 2)

print(answer)
