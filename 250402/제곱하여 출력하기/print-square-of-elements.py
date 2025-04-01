N = int(input())
num = map(int, input().split())

result = [x ** 2 for x in num]
print(*result, sep=' ')