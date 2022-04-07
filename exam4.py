#4-masala
n=int(input("n = "))
i=0
j=0
max=float(input())
for x in range(1,n):
    k=float(input())
    if max<k:
        j=x
        i=x
        max=k
    elif max ==k:
        j=x
if i!=j:
    print(i,j)
else:
    print(i)