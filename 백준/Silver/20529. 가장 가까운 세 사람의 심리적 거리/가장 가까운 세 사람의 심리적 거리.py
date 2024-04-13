import sys
input = sys.stdin.readline

def distance(mbti):
    d = 0
    for i in range(4):
        if mbti[0][i] != mbti[1][i]:
            d += 1
        if mbti[1][i] != mbti[2][i]:
            d += 1
        if mbti[2][i] != mbti[0][i]:
            d += 1
    return d

T = int(input())

for _ in range(T):
    N = int(input())
    MBTI = input().split()

    if N > 32:
        print(0)
    else:
        min_distance = 12
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    min_distance = min(distance([MBTI[i], MBTI[j], MBTI[k]]), min_distance)
        print(min_distance)