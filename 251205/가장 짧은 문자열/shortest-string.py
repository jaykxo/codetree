import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()
c = input().strip()
temp = [len(a), len(b), len(c)]

longest = max(temp)
shortest = min(temp)

print(longest - shortest)