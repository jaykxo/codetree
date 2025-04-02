start, end = map(int, input().split())
count = 0

for i in range(start, end + 1):
    div_count = 0

    for j in range(1, i + 1):
        if i % j == 0:
            div_count += 1

    if div_count == 3:
            count += 1

print(count)