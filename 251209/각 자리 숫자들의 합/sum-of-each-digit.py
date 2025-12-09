import sys
input = sys.stdin.readline

nums = list(map(str, input().strip()))

cnt = 0
for num in nums:
    cnt += int(num)

print(cnt)