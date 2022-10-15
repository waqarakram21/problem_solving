s = str(input())
if s[2]=="A" or s[2]=="E"or s[2]=="I"or s[2]=="O"or s[2]=="U":
    print("invalid")
elif (int(s[0])+int(s[1]))%2==0 and (int(s[3])+int(s[4]))%2==0 and (int(s[5])+int(s[6]))%2==0 and(int(s[7])+int(s[8]))%2==0:
    print("valid")
else:
    print("invalid")
