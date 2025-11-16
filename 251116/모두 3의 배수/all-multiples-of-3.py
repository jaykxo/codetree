import sys
input = sys.stdin.readline

three = True

for i in range(5):
    N = int(input())
    if N % 3 != 0:
        three = False

if three:
    print(1)
else:
    print(0)
