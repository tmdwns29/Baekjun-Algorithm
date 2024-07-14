import sys
input = sys.stdin.readline

check = 'Was it a cat I saw?'
sentence =''

i = 2
while True:
    sentence = input().rstrip()

    if sentence == check: break
    print(sentence[::i])
    i+=1