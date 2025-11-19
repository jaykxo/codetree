import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

arr = [i ** 2 for i in nums]

print(" ".join(map(str, arr)))