import sys
input = sys.stdin.readline

words = list(map(str, input().split()))

for word in words[0::2]:
    print(word)