n=int(input("n = "))
a=[]
for x in range(n):
    a.append(int(input("a = ")))
    if x!=a.index(a[x]):
        i=a.index(a[x])
        j=x
print(i, "va", j)