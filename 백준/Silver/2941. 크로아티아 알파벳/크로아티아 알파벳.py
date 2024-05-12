import sys
input = sys.stdin.readline

word = input().rstrip()
ck = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in ck:
    word = word.replace(i, '$')
print(len(word))