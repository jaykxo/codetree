import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0

for i in range(N):
    if num[i] == M:
        cnt += 1

print(cnt)