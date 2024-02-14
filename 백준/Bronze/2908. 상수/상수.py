n, m = input().split()

if n[::-1] > m[::-1]:
    print(n[::-1])
else:
    print(m[::-1])
