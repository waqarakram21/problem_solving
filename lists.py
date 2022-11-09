if __name__ == '__main__':    
    arr=list(int,input().strip().split())
    operation=str(input())
    if operation=='insert':
        inserted=input().rstrip().split()
        operation=str(inserted[0])

        i=int(inserted[1])
        e=int(inserted[2])
        arr.insert(e,i)
    elif operation=='print':
        print(arr)
    # elif operation=='append':
        

    