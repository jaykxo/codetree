import sys
input = sys.stdin.readline

word, ch = input().split()

if ch in word:
    print(word.index(ch))
else:
    print("No")