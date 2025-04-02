while True: 
    try:
        N = int(input())
    except EOFError:
        break
    except ValueError:
        continue

    if N < 25:
        print("Higher")
    elif N > 25:
        print("Lower")
    else:
        print("Good")
    
