import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
cur = n

while cnt < 2:
    print(cur, end=' ')
    if cur % 5 == 0:
        cnt += 1
    cur += n