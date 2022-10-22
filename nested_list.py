from numpy import double


if __name__ == '__main__':
    N = int(input())

    list=[]
    for i in range(N):
        name=input()
        score=float(input())
        list.append([name,score])

    list2=[]
    # print(list)
    
    for j in range(len(list)):
        list2.append(list[j][1])
    new_list=set(list2)
    new_list.remove(min(list2))
    # print(new_list)
    scndmx=min(new_list)
    # print(scndmx)
    final_list=[]
    for k in range(len(list)):
        if list[k][1]==scndmx:
            final_list.append(list[k][0])

    sorted_list=sorted(final_list)
    for word in range(len(sorted_list)):
        print(sorted_list[word])

