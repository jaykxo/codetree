import sys
input = sys.stdin.readline

N = int(input())
words = []
for _ in range(N):
    words.append(input().strip())
cnt = 0
length = []

for word in words:
    length.append(len(word))
    if word[0] == "a":
        cnt += 1

print(sum(length), cnt)