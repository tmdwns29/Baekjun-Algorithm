import math
cnt=0
for i in range (int(input())+1):
    cnt+=1/math.factorial(i)
print(cnt)