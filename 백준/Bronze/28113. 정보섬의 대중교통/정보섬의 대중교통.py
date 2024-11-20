N, A, B = map(int, input().split())

if N + (B-N) > A:
    print('Bus')
elif N + (B-N) < A:
    print('Subway')
else:
    print('Anything')