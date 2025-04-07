a, b, c = map(int, input().split())

def minimum(a, b, c):
    min_value = a
    if min_value > b:
        b = min_value
    if min_value > c:
        c = min_value
    print(min_value)
    
minimum(a, b, c)