import sys
input = sys.stdin.readline

ch1, ch2 = input().split()

a = ord(ch1)
b = ord(ch2)

print(a + b, abs(a - b))