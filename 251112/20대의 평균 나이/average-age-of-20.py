nums = []

while True:
    n = int(input())
    if n // 10 != 2:
        break
    else:
        nums.append(n)

avg = sum(nums) / len(nums)
print(f"{avg:.2f}")