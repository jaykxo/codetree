import sys
input = sys.stdin.readline

a = list(map(str, input().split()))
b = list(map(str, input().split()))

new = a + b

print(''.join(map(str, new)))
