n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
min_val = 2**31 - 1
cnt = 0

for num in nums:
    if num == min_val:
        cnt += 1
    elif num < min_val:
        min_val = num
        cnt = 1

print(min_val, cnt)