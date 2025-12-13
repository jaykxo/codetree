import sys
input = sys.stdin.readline

A = list(map(str, input().strip()))
B = list(map(str, input().strip()))
cnt = 0


for _ in range(len(A)):
    if A == B:
        break
    A = A[1:] + [A[0]]
    cnt += 1

if A != B:
    cnt = -1

print(cnt)