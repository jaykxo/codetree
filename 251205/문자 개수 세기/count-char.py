import sys
input = sys.stdin.readline

arr = list(map(str, input().strip()))
ch = input().strip()

cnt = 0

for i in range(len(arr)):
    if arr[i] == ch:
        cnt += 1

print(cnt)