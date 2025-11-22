import sys
input = sys.stdin.readline

N = int(input())
arr = [1, N]

while True:
    cur = arr[-1] + arr[-2]
    arr.append(cur)
    if cur >= 100:
        break
    
print(' '.join(map(str, arr)))