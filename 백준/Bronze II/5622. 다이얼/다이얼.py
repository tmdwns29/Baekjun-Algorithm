a = {2:'ABC', 3:'DEF', 4:'GHI',
     5:'JKL', 6:'MNO', 7:'PQRS',
     8:'TUV', 9:'WXYZ'}

arr = input()
num = 0
for i in arr:
    for j in range(2,10):
        if i in a[j]:
            num += j+1

print(num, end='')