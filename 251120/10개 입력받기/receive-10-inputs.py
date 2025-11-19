import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))
arr = []

for num in nums:
    if num == 0:
        break
    arr.append(num)

avg = sum(arr) / len(arr)

print(sum(arr), f"{avg:.1f}")