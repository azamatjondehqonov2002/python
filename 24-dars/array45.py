n=int(input("n = "))
a=[]
i=0
j=1
min=-1
for x in range(n):
    a.append(int(input()))
    if x>0 and min>=0 and abs(a[x]-a[x-1])<min:
        min=abs(a[x]-a[x-1])
        i=x
        j=x-1
    elif x>0 and min==-1:
        min = a[x]-a[x-1]

print(i, "va", j)