import sys
input = sys.stdin.readline

ch = input().strip()
fruits = ["apple", "banana", "grape", "blueberry", "orange"]
cnt = 0

for fruit in fruits:
    if fruit[2] == ch or fruit[3] == ch:
        print(fruit)
        cnt += 1

print(cnt)