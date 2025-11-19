import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
acc = 0
cnt = 0

for i in range(len(arr)):
    if arr[i] >= 250:
        break
    else:
        acc += arr[i]
        cnt += 1

avg = acc / cnt

print(acc, f"{avg:.1f}")