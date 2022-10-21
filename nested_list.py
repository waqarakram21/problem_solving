if __name__ == '__main__':
    N = int(input())

    list=[]
    for i in range(N):
        name=input()
        score=input()
        list.append([name,score])

    list2=[]
    # print(list)
    
    for j in range(len(list)):
        list2.append(list[j][1])
    new_list=set(list2)
    new_list.remove(max(list2))
    scndmx=max(list2)
    # print(scndmx)

    for k in range(len(list)):
        if list[k][1]==scndmx:
            print(list[k][0])
