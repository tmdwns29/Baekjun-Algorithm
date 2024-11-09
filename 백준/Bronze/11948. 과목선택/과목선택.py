import sys
input = sys.stdin.readline

subject_1 = list()
subject_2 = list()

for _ in range(4):
    subject_1.append(int(input()))
for _ in range(2):
    subject_2.append(int(input()))

subject_1 = sorted(subject_1)

print(sum(subject_1[:-4:-1])+max(subject_2))