import sys
input = sys.stdin.readline

word = input().strip()
ch = input().strip()
cnt = 0

for i in range(len(word) - 1):
    if word[i] == ch[0] and word[i + 1] == ch[1]:
        cnt += 1

print(cnt)