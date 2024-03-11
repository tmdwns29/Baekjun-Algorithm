import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
pokemon=[]
for i in range(N):
    pokemon.append(input().rstrip())
for i in range(M):
    search = input().rstrip()
    if 65<=ord(search[0])<=90:
        print(pokemon.index(search)+1)
    else:
        search=int(search)
        print(pokemon[search-1])