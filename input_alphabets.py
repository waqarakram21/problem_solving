S =str(input())
new_s = ""
for i in S:
    if i.isupper() == True:
        new_s += i.lower()
    elif i.islower() == True:
        new_s += i.upper()
    elif i.isspace() == True:
        new_s += i

print(new_s)
