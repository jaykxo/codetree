import sys
input = sys.stdin.readline

word = input().strip()

if 'ee' in word:
    ee = "Yes"
else:
    ee = "No"

if 'ab' in word:
    ab = "Yes"
else:
    ab = "No"

print(ee, ab)