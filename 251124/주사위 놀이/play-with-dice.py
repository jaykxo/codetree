import sys
input = sys.stdin.readline

dice = list(map(int, input().split()))
cnt = [0] * 7

for x in dice:
    cnt[x] += 1

for i in range(1, 7):
    print(f"{i} - {cnt[i]}")