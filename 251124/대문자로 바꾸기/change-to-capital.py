import sys
input = sys.stdin.readline

for _ in range(5):
    arr = input().split()
    arr = [s.upper() for s in arr]
    print(' '.join(map(str, arr)))