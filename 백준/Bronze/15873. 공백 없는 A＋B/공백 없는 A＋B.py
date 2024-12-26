num = input()

if len(num) == 2:
    print(int(num[0])+int(num[1]))
elif len(num) == 3:
    if num[1] == '0':
        print(int(num[0]+num[1])+int(num[2]))
    elif num[2] == '0':
        print(int(num[0])+int(num[1]+num[2]))
else:
    print(int(num[0]+num[1])+int(num[2]+num[3]))