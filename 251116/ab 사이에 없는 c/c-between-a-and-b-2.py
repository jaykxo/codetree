import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
multiple = True

for i in range(a, b + 1):
    if i % c == 0:
        multiple = False

if multiple:
    print("YES")
else:
    print("NO")