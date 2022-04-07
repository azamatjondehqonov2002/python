n=int(input("n = "))
R=int(input("R = "))
a=[]
i=0
j=1
for x in range(n):
    a.append(int(input("a = ")))
    if x==1:
        min=abs(R-a[x]-a[x-1])
    elif x>1:
        if abs(R-a[x]-a[x-1])<min:
            i=x
            j=x-1
print(a[i]," va ",a[j])