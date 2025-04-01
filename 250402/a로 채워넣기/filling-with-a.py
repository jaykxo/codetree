word = list(input())
word[1] = "a"
word[-2] = "a"

print(*word, sep='')