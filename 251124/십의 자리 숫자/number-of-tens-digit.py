import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
cnt = [0] * 10

for x in arr:
    if x == 0:
        break
    x //= 10
    cnt[x] += 1

for i in range(1, 10):
    print(f"{i} - {cnt[i]}")