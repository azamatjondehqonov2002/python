#2-masala
def butun(a,b):
    i=0
    while a>=b:
        a-=b
        i+=1
    return i

a = int (input("a = "))
b = int (input("b = "))
k=butun(a,b)
q=a-k*b
print(k, " chiqib ",q," qoldiq qoladi.")