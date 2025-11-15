import sys
input = sys.stdin.readline

N = int(input())
composite = False

for i in range(2, N):
    if N % i == 0:
        composite = True 

if composite:
    print("C")
else:
    print("N")