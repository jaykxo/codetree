import sys
input = sys.stdin.readline

a, b = map(int, input().split())
arr= []
temp = 0

for i in range(10):
    if i == 0:
        arr.append(a)
    elif i == 1:
        arr.append(b)
    else:
        temp = arr[i - 2] + arr[i - 1]
        if temp >= 10:
            temp -= 10
        arr.append(temp)

print(' '.join(map(str, arr)))