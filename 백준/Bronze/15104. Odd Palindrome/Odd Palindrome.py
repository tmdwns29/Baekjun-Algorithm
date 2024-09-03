import sys
input = sys.stdin.readline

S = input().rstrip()

def is_palindrome(l, r):
    while l < r:
        if S[l] != S[r]:
            return False
        l += 1
        r -= 1
    return True

for i in range(len(S)):
    for j in range(i, len(S)):
        if is_palindrome(i, j):
            if (j - i + 1) % 2 == 0:
                print('Or not.')
                exit(0)
print('Odd.')