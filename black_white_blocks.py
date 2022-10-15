t = int(input())
for i in range(t):
    n,m = [int(x) for x in input().split()]
    max = 0
    for i in range(n):
        y = input()
        j = y.count('#')
        if j > max :
            max = j
    print(max)