import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
two = []
three = []

for i in range(0, 10):
    if i % 2 == 1:
        two.append(arr[i])
    if i % 3 == 2:
        three.append(arr[i])

print(sum(two), f"{(sum(three) / len(three)):.1f}")