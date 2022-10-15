L = float(input("Length: "))
N = int(input("Number of photos: "))

for _ in range(N):
    W,H= map(int,input().split())
    if W < L or H < L:
        print("UPLOAD ANOTHER")
    elif W == H:
        print("ACCEPTED")
    else:
        print("CROP IT")