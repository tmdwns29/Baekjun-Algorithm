A, I = map(int, input().split())

melody = A*I

while I-1 < melody / A <= I:
    melody -= 1
print(melody+1)