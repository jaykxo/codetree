N = int(input())
num = list(map(int, input().split()))
new = []

for i in num:
    if i != 1 and i % 2 == 0:
        new.append(i)

new.reverse()
print(*new, sep=' ')