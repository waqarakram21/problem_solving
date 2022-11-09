n=int(input())
t=(input())
tuple=tuple(int(item) for item in t.split())[:n]
print(hash(tuple))