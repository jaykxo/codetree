import sys
input = sys.stdin.readline

word = input().strip()
ch = input().strip()

if ch in word:
    print(word.index(ch))
else:
    print(-1)