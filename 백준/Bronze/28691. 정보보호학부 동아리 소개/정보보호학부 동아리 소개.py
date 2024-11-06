import sys
input = sys.stdin.readline

C = input().rstrip()

if C == 'M': print('MatKor')
elif C == 'W': print('WiCys')
elif C == 'C': print('CyKor')
elif C == 'A': print('AlKor')
elif C == '$': print('$clear')