import sys
input = sys.stdin.readline

a, b = list(map(int, input().split()))
arr = [a, b]

while len(arr) < 10:
    cur = arr[-1] + 2 * arr[-2]
    arr.append(cur)

print(' '.join(map(str, arr)))