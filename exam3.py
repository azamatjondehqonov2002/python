a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
if a<b and b<c:
    print(b)
elif a<c and c<b:
    print(c)
else:
    print(a)