import sys

while True:
    n = int(sys.stdin.readline())
    if n == 25:
        print("Good")
        break
    if n < 25:
        print("Higher")
    elif n > 25:
        print("Lower")