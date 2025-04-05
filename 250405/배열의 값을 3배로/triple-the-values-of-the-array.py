matrix = []

for i in range(3):
    row = []
    nums = input().split()
    for j in range(3):
        row.append(int(nums[j]) * 3)
    matrix.append(row)

for row in matrix:
    print(*row)