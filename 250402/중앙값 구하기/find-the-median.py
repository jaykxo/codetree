A, B, C = map(int, input().split())

if A > B:
    if B > C:
        med = B
    elif A > C:
        med = C
    else:
        med = A

else:
    if A > C:
        med: A
    elif B > C:
        med = C
    else:
        med = B

print(med)
