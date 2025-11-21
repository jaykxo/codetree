import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
even = []

for num in nums:
    if num % 2 == 0:
        even.append(num)

print(' '.join(map(str, even)))