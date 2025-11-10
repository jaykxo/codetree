N = int(input())

for i in range(1, N + 1):
    N //= i
    if N <= 1:
        print(i)
        break