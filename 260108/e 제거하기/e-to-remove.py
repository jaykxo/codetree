arr = list(map(str, input().strip()))

for i in range(len(arr)):
    if arr[i] == "e":
        arr.pop(i)
        break

print(''.join(arr))