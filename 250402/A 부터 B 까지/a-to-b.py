A, B = map(int, input().split())
result = [A]

while A < B:
    if A % 2 == 1:
        A = A * 2
    else:
        A = A + 3
    
    if A > B:
        break
    result.append(A)

print(*result, end=' ')