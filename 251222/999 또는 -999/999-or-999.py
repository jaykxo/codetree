import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))
arr = []

for i in range(len(nums)):
    if nums[i] == 999 or nums[i] == -999:
        break
    arr.append(nums[i])

print(max(arr), min(arr))