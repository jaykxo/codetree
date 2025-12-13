import sys
input = sys.stdin.readline

words = []

for _ in range(200):
    new = input().strip()
    if new == "0":
        break
    words.append(new)

print(len(words))

for i in range(len(words)):
    if i % 2 == 0:
        print(words[i])