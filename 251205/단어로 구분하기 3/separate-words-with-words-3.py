import sys
input = sys.stdin.readline

words = list(map(str, input().split()))

for word in words[::-1]:
    print(word)