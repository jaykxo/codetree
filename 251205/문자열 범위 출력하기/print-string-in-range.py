import sys
input = sys.stdin.readline

ch = input()
new = []

for i in range(2, 10):
    new.append(ch[i])

print(''.join(map(str, new)))