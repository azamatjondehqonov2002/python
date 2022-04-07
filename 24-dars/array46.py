n=int(input("n = "))
R=int(input("R = "))
a=[]
for x in range(n):
    a.append(int(input("a = ")))
i=0
j=1
min=abs(R-a[i]-a[j])
for x in range(n-1):
    for y in range(x+1,n):
        if abs(R-a[x]-a[y])<min:
            i=x
            j=y
print(a[i]," va ",a[j])