while True:
    try:
        n = int(input())
    except EOFError:
        break
    if n % 2 == 1:
        continue
    else:
        print(n // 2)