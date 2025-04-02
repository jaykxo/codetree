N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    even = []

    for i in range(a, b + 1):
       if i % 2 == 0:
           even.append(i) 
    print(sum(even))