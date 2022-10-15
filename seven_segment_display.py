t= int(input())
i=0
matchsticks={0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
while i<t:
    num=input()
    no_of_matchsticks=0
    i+=1

for totalsticks in range(num):
    no_of_matchsticks += matchsticks[int(totalsticks)]
    if no_of_matchsticks%2==0:
        print("1"*no_of_matchsticks//2)
    elif no_of_matchsticks%2!=0:
        a= int(no_of_matchsticks-3)//2
        print("7"+("1")*a)
        i+=1