num = list(map(int, input().split()))

while len(num) < 10:
    new_num = num[-1] + num[-2]
    if new_num >= 10:
        new_num = new_num % 10
    num.append(new_num)
print(*num, sep=' ')
