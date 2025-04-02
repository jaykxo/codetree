num = []
three = []
five = []

for _ in range(10):
    num.append(int(input()))

for i in num:
    if i % 5 == 0:
        five.append(i)
    if i % 3 == 0:
        three.append(i)

print(len(three), len(five))