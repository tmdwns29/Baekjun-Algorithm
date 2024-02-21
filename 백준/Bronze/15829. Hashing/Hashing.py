L = int(input())
arr = input()
result = 0

for i in range(L):
    result += (ord(arr[i])-96)*(31**i) # ord()->아스키코드값 반환
print(result % 1234567891) # M = 1234567891