import sys
input = sys.stdin.readline

word = list(map(str, input().strip()))
f = word[0]
s = word[1]

for i in range(len(word)):
    if word[i] == s:
        word[i] = f

print(''.join(map(str, word)))