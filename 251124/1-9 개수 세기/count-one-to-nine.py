import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

cnt = [0] * 10

for x in nums:
    cnt[x] += 1

for i in range(1, 10):
    print(cnt[i])