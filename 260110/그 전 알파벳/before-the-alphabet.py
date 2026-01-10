import sys
input = sys.stdin.readline

ch = input().strip()
num = ord(ch)
num -= 1

if ch == "a":
    print("z")
else:
    print(chr(num))