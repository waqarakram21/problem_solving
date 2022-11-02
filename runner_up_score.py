if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max=max(arr)
    # print(max)
    arr1=[]
    for i in arr:
        # print(i)
        if i==max:
            pass
        else:
            arr1.append(i)
    arr1_max=arr1[0]
    for j in arr1:
        if j>arr1_max:
            arr1_max=j
    print(arr1_max)            