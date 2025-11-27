import sys
input = sys.stdin.readline

ch = input().strip()

if ch == "z":
    print("a")
else:
    ch = ord(ch)
    ch += 1
    ch = chr(ch)
    print(ch)