letter = input()
fruits = ['apple', 'banana', 'grape', 'blueberry', 'orange']
result = []

for fruit in fruits:
    if fruit[2] == letter or fruit[3] == letter:
        result.append(fruit)

if result:
    print(*result, sep='\n')
    print(len(result))
else:
    print(0)