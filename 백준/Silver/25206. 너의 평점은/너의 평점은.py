import sys
input = sys.stdin.readline
rank = 0
cnt = 20
major_sum = 0
score = 0

for i in range(20):
    major = input().rstrip().split()
    if major[2] == 'A+': rank = 4.5
    elif major[2] == 'A0': rank = 4.0
    elif major[2] == 'B+': rank = 3.5
    elif major[2] == 'B0': rank = 3.0
    elif major[2] == 'C+': rank = 2.5
    elif major[2] == 'C0': rank = 2.0
    elif major[2] == 'D+': rank = 1.5
    elif major[2] == 'D0': rank = 1.0
    elif major[2] == 'F': rank = 0.0
    else : continue
    score += float(major[1])*rank
    major_sum += float(major[1])
print(score/major_sum)