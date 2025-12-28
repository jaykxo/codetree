N = int(input())

for i in range(N, 0, -1):
    y = N - i
    for j in range(y):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()
    
for i in range(2, N + 1):
    y = N - i
    for j in range(y):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()