import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
arr = []

for num in nums:
    if num % 2 == 0:
        arr.append(num)

print(" ".join(map(str, arr[::-1])))