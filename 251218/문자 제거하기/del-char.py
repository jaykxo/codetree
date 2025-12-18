import sys
input = sys.stdin.readline

word = list(map(str, input().strip()))

for _ in range(len(word) - 1):
    n = int(input())
    if n < len(word):
        word.pop(n)
    else:
        word.pop(-1)

    print(''.join(map(str, word)))
