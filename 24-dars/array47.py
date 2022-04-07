n=int(input())
a=[]
b=[]
for x in range(n):
    a.append(int(input("a = ")))
    if b.count(a[x])==0:
        b.append(a[x])
    
print(a)
print(b)