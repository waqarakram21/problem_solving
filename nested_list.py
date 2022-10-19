name = input()
scores= float(input())
rows=[]
columns=[]
        
for i in range(name):
    for j in range(scores):
        columns.append(input())
    rows.append(columns)
    columns=[]
    print(rows)




        