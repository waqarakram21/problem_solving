l,r,k= map(int,input().split())
counter=0
for i in range(l,r+1):
    if i%k==0:
        counter+=1
    
print(counter)
