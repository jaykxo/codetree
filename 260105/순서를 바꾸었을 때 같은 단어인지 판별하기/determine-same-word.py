word1 = list(map(str, input().strip()))
word2 = list(map(str, input().strip()))

# Please write your code here.
word1.sort()
word2.sort()

if word1 == word2:
    print("Yes")
else:
    print("No")