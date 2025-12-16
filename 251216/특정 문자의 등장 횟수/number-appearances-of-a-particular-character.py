import sys
input = sys.stdin.readline

word = input().strip()

ee = 0
eb = 0

for i in range(len(word) - 1):
    if word[i] == 'e' and word[i + 1] == 'e':
        ee += 1
    if word[i] == 'e' and word[i + 1] == 'b':
        eb += 1

print(ee, eb)