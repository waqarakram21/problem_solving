arr=list(map(int,input().strip().split()))
new_arr=(set(arr))
new_arr.remove(max(new_arr))
print(max(new_arr))