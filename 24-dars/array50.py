from random import randint

n=int(input("n = "))
a=[]
b=[]
for x in range(n):
    a.append(randint(-10**5,10**5))
    if x>0 and a[x]<a[x-1]:
        b.append(a[x-1])
print(a)
print(b)