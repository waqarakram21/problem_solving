for t in range(int(input())):
    green,purple= map(int,input().split())
    cost=0
    q1c,q2c=0,0
    for n in range(int(input())):
        q1,q2=map(int,input().split())
        if q1==1:
            q1c = q1c+1
        if q2==1:
            q2c = q2c +1
    if green > purple:
        if q1c>q2c:
            c=green*q2c + purple*q1c
        else:
            c= purple*q2c + green*q1c
    else:
        if q1c>q2c:
            c= green*q1c + purple*q2c
        else:
            c = purple*q1c + green*q2c
    print(c)