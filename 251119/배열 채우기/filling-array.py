import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
new = []

for i in range(10):
    if arr[i] == 0:
        break
    else:
        new.append(arr[i])

print(" ".join(map(str, new[::-1])))