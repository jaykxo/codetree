import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
new = []

for i in range(100):
    if arr[i] == 0:
        break
    new.append(arr[i])

for i in range(len(new)):
    if new[i] % 2 != 0:
        new[i] += 3
    else:
        new[i] //= 2

print(' '.join(map(str, new)))