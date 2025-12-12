import sys
input = sys.stdin.readline

for _ in range(100):
    new = input().strip()
    if new == "END":
        break
    print(new[::-1])