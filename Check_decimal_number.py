from sqlalchemy import false

T=int(input("enter the length of the string: "))
def Check_Integer (N):
    for i in range(T):
        if (N.isdigit()== False):
            return False
    return True

N=input("enter the string: ")
if (Check_Integer(N)==True):
    print("Yes")
else:
    print("NO")