import sys
input = sys.stdin.readline  

cnt, num = 0,0
for i in range(1, 4):
    word = input().rstrip()
    if word in 'FizzBuzz':
        continue
    num = int(word)
    cnt = i

if cnt == 1:
    num += 3
elif cnt == 2:
    num += 2
elif cnt == 3:
    num += 1

if num%3==0 and num%5==0:
    print('FizzBuzz')
elif num%3==0 and num%5!=0:
    print('Fizz')
elif num%3!=0 and num%5==0:
    print('Buzz')
else:
    print(num)