def ekub(a,b):
    if b>a:
        a,b = b,a
    while a%b!=0:
        a=a%b
        if b>a:
            a,b = b,a
    return b

a=int(input("a = "))
b=int(input("b = "))
print(ekub(a,b))