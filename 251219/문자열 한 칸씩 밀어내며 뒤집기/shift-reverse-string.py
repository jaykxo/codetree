import sys
input = sys.stdin.readline

arr, q = input().split()
q = int(q)

for _ in range(q):
    n = int(input())
    if n == 1:
        arr = arr[1:] + arr[0]
        print(arr)
    elif n == 2:
        arr = arr[-1] + arr[:-1]
        print(arr)
    else:
        arr = arr[::-1]
        print(arr)