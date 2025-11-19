import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))
odd = []
even = []

for i in range(10):
    if i % 2 == 0:
        odd.append(nums[i])
    else:
        even.append(nums[i])

result = sum(odd) - sum(even)

print(abs(result))