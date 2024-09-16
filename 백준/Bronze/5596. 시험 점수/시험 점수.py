import sys
input = sys.stdin.readline

Minkook = list(map(int, input().split()))
Mansae = list(map(int, input().split()))

Minkook_score = sum(Minkook)
Mansae_score = sum(Mansae)

print(Minkook_score if Minkook_score >= Mansae_score else Mansae_score)