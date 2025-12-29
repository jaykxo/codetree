N = int(input())

# Please write your code here.
for i in range(1, N + 1):
    y = N - i
    for j in range(y):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
for i in range(N - 1, 0, -1):
    y = N - i
    for j in range(y):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()