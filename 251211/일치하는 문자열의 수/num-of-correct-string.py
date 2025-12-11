import sys
input = sys.stdin.readline

n, A = input().split()
n = int(n)
words = []
cnt = 0

for _ in range(n):
    words.append(input().strip())

for word in words:
    if word == A:
        cnt += 1

print(cnt)