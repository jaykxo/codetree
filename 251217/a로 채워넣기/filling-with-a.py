import sys
input = sys.stdin.readline

word = list(map(str, input().strip()))

word[1] = 'a'
word[-2] = 'a'

print(''.join(map(str, word)))