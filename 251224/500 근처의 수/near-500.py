import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))
over = []
under = []

for num in nums:
    if num > 500:
        over.append(num)
    elif num < 500:
        under.append(num)

print(max(under), min(over))