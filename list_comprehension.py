if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
coordi=[[x,y,z] for X in range(x) for Y in range(y) for Z in range(z) if x+y+z!=n] 
for i in range(n):
    print(coordi[i])