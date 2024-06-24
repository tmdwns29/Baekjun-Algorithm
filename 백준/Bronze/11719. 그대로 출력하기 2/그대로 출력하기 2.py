i=0
while i<100:
    try:
        print(input())
    except EOFError:
        break