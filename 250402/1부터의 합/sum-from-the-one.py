N = int(input())
num = 0

for i in range(1, 101):
    num = num + i
    if N > num:
        continue
    else:
        break

print(i)