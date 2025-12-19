import sys
input = sys.stdin.readline

word = input().strip()

print(word)

for _ in range(len(word)):
    word = word[-1] + word[:-1]
    print(word)