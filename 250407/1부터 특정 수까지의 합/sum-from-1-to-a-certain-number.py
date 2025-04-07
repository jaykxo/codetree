def sth():
    count = 0
    for i in range(1, N + 1):
        count += i
        result = count // 10
    print(result)

N = int(input())
sth()