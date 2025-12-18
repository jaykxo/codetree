import sys
input = sys.stdin.readline

word = list(map(str, input().strip()))

word.pop(1)
word.pop(-2)

print(''.join(map(str, word )))