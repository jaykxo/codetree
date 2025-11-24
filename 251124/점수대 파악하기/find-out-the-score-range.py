import sys
input = sys.stdin.readline

score = list(map(int, input().split()))
cnt = [0] * 11

for x in score:
    if x == 0:
        break
    x //= 10
    cnt[x] += 1

for i in range(10, 0, -1): 
    print(f"{i}0 - {cnt[i]}")