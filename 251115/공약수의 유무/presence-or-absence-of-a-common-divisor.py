import sys
input = sys.stdin.readline

A, B = map(int, input().split())
exist = False

for i in range(A, B + 1):
    if 1920 % i == 0 and 2880 % i == 0:
        exist = True

if exist:
    print(1)
else:
    print(0)