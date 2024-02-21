N = int(input())
arr = input()
alphabet = ' abcdefghijklmnopqrstuvwxyz'

def Hash(num, x):
    result = 0
    for i in range(1, num+1):
        for j in alphabet:
            if x[i-1] == j:
                result += alphabet.index(j)*(31**(i-1))
    return result

print(Hash(N,arr))