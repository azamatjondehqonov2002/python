import random


n=int(input("n = "))
a=[]
b=[]
for x in range(n):
    a.append(random.randint(-10**5,10**5))
    b.append(random.randint(-10**5,10**5))
print(a,b)
a,b=b,a
print(a,b)