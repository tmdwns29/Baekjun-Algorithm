import sys
input = sys.stdin.readline

jaehwan = input().rstrip()
doctor = input().rstrip()

if jaehwan.count('a') >= doctor.count('a'):
    print('go')
else:
    print('no')