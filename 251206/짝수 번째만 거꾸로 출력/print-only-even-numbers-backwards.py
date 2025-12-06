import sys
input = sys.stdin.readline

arr = list(map(str, input().strip()))
even = []

for i in range(len(arr)):
    if i % 2 == 1:
        even.append(arr[i])

even = even[::-1]
print(''.join(map(str, even)))