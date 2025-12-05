import sys
input = sys.stdin.readline

words = []
for _ in range(10):
    words.append(input().strip())
ch = input().strip()
new = []

for word in words:
    if word[-1] == ch:
        new.append(word)

if new:
    print('\n'.join(map(str, new)))
else:
    print("None")