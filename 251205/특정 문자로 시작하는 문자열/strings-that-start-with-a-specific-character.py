import sys
import statistics
input = sys.stdin.readline

N = int(input())
words = []
for _ in range(N):
    words.append(input().strip())
ch = input().strip()
included = []
length = []

for word in words:
    if word[0] == ch:
        included.append(word)
        length.append(len(word))

avg = statistics.mean(length)

print(len(included), f"{avg:.2f}")