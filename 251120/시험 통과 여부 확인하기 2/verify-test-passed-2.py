import sys
input = sys.stdin.readline

n = int(input())
p = 0

for _ in range(n):
    score = list(map(int, input().split()))
    avg = sum(score) / 4

    if avg >= 60:
        print("pass")
        p += 1
    else:
        print("fail")

print(p)