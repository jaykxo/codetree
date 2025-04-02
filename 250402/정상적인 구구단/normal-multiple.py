n = int(input())

for i in range(1,n+1):
    mult = []
    for j in range (1,n+1):
        mult.append(f"{i} * {j} = {i*j}")
    print(", ".join(mult))