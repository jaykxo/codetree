import sys
input = sys.stdin.readline

a = input()
b = input()
c = input()
temp = [len(a), len(b), len(c)]

longest = max(temp)
shortest = min(temp)

print(longest - shortest)