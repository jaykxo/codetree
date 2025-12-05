import sys
input = sys.stdin.readline

words = []
for _ in range(4):
    words.append(input().strip())

for word in words[::-1]:
    print(word)