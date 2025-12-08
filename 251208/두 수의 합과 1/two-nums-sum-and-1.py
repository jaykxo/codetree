import sys
input = sys.stdin.readline

a, b = map(int, input().split())

result = a + b
result = str(result)
cnt = 0

for i in result:
    if i == "1":
         cnt += 1

print(cnt)