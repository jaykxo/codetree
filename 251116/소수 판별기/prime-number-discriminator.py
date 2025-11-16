import sys
input = sys.stdin.readline

N = int(input())
prime = True

for i in range(2, N):
    if N % i == 0:
        prime = False

if prime:
    print("P")
else:
    print("C")