nonzero = []

while True:
    n = int(input())
    if n == 0:
        break
    nonzero.append(n)

print(*nonzero, sep='\n')