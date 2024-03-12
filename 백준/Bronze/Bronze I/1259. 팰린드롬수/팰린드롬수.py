while True:
    N = list(map(int, input()))
    num = 0
    for i in range(len(N)//2):
        if N[i] == N[len(N)-i-1]:
            num += 1
    if N == [0]: break
    elif num == len(N)//2:
        print('yes')
    else:
        print('no')
