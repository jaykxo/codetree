import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))
arr = []

for num in nums:
    if num == 0:
        break
    elif num % 2 == 0:
        arr.append(num)

print(len(arr), sum(arr))