def fac(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fac(n-1)
    
n=int(input("n = "))
x=float(input("x = "))
s=0
i=0

for i in range(n+1):
    s+=(-1)**i*x**(2*i+1)/fac(2*i+1)

print("s = ",s)