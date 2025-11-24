import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

for i in range(len(arr)):
    arr[i] //= 10

cnt = [0] * 10

for x in arr:
    cnt[x] += 1

for i in range(1, 10):
    print(f"{i} - {cnt[i]}")