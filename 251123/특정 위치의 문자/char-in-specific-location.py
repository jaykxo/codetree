import sys
input = sys.stdin.readline

arr = ["L", "E", "B", "R", "O", "S"]
a = input().strip()

idx = -1   

for i in range(len(arr)):
    if arr[i] == a:
        idx = i
        break

if idx == -1:
    print("None")
else:
    print(idx)