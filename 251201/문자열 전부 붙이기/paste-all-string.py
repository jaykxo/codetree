import sys
input = sys.stdin.readline

n = int(input())
arr = ""

for _ in range(n):
    word = input().rstrip()
    arr += word

print(arr)