import sys
input = sys.stdin.readline

ch = input().strip()
N = int(input())
new = []

for elem in ch[::-1][:N]:
    new.append(elem)

print(''.join(map(str, new))) 