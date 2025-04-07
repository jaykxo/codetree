n = input()

def something(n):
    sum = int(n[0]) + int(n[1])
    return int(n) % 2 == 0 and sum % 5 == 0

if something(n):
    print("Yes")
else:
    print("No")