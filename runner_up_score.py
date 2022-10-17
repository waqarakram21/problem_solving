if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    run=arr[0]
    for i in arr:
        if i > run:
            run = i
    
            ndrun= arr.index(run)
            del(arr[ndrun])
    print(run)