import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))

num = 1
for i in range(N):
    row = []
    for j in range(M):
        row.append(num)
        num += 1
    print(*row)
