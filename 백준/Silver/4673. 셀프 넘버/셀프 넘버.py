num = list(range(1, 10001))

def d(n):
    number = str(n)

    for i in number:
        n += int(i)
    
    if n in num:
        num.remove(n)

for a in range(1, 10001):
    d(a)
for b in num:
    print(b)