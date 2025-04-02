N = int(input())
num = 1

for i in range(1, 101):
    num = num + i
    if N > num:
        continue
    if N <= num:
        break

print(i)

