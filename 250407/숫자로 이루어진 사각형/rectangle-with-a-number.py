N = int(input())

def sth():
    cnt = 1
    for _ in range(N):
        for _ in range(N):
            print(cnt, end=' ')
            cnt += 1
            if cnt == 10:
                cnt = 1
        print()
sth()
