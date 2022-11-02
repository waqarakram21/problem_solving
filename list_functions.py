if __name__ == '__main__':
    N = int(input())
    list=[]
    match N:
        case 1:
            e=int(input())
            i=int(input())
            list.insert(e,i)
            # print(list)
        case 2:
            print("print the list.")
        case 3:
            print("remove the first occurence of element e.")
        case 4:
            print("insert e at the end of the list.")
        case 5:
            print("sort the list.")
        case 6:
            print("pop the list element from the list.")
        case 7:
            print("reverse the list.")