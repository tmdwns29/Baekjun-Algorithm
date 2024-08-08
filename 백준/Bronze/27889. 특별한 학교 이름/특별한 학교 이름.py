import sys
input = sys.stdin.readline

school = ['North London Collegiate School',
          'Branksome Hall Asia',
          'Korea International School',
          'St. Johnsbury Academy']
result = ''
word = input().rstrip()
if word == 'NLCS':
    result = school[0]
elif word == 'BHA':
    result = school[1]
elif word == 'KIS':
    result = school[2]
elif word == 'SJA':
    result = school[3]
print(result)