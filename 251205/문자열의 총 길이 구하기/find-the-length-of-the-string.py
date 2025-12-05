import sys
input = sys.stdin.readline

words = list(map(str, input().split()))
length = []

for word in words:
    length.append(len(word))

print(sum(length))