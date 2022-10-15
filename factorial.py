n = int(input())
fact=1
if n == 0:
        print("the factorial dosen't exist...")
elif n==1:
        print("the factorial is 1...")
else:
        for i in range(1,n+1):
                fact=fact*i
        print(f"the factorial of number is {fact}")