import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    for i in range(N):
        print(i + 1, end="")
    print()