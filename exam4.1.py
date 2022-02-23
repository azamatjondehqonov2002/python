n=int(input("n = "))
x=float(input("x = "))
s=0
i=0
j=1
k=1
for i in range(n+1):
    while j<=2*i+1:
        k*=j
        j+=1
    s+=(-1)**i*x**(2*i+1)/k
    j=1
    k=1
print("s = ",s)