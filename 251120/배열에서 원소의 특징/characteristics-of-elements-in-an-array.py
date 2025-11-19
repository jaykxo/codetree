import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))
arr = []

for num in nums: 
    if num % 3 == 0:
        break
    arr.append(num)

print(arr[len(arr) - 1])