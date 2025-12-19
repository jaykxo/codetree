import sys
input = sys.stdin.readline

arr = input().strip()
arr = arr[1:] + arr[0]

print(arr)