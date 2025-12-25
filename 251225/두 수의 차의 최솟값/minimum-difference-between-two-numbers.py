import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
min_diff = nums[1] - nums[0]

for i in range(1, N):
    if nums[i] - nums[i - 1] < min_diff:
        min_diff = nums[i] - nums[i - 1]

print(min_diff)