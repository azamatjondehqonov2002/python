n=int(input())
a=[]
for x in range (n):
    a.append(int(input("a = ")))

maxin=0
a.sort()
m=1
for x in range(1,n):
    if a[x]!=a[x-1]:
        m=1
    else:
        m+=1
    if m > maxin:
            maxin=m
print(maxin)