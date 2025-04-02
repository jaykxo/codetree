N = int(input())
unfam = []

for i in range(1, N+1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    unfam.append(i)
print(len(unfam))