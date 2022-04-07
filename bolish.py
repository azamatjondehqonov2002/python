a=float(input("a = "))
b=float(input("b = "))
n=int(input("Necha xonagacha aniqlikda hisoblashni hohlaysiz?\nn = "))
s=""
i=0
if b!=0:
    print(a," : ",b," = ", end="")
if a>0 and b<0 or a<0 and b>0:
    s+="-"
a=abs(a)
b=abs(b)
if b!=0:
    while a>=b:
        i+=1
        a-=b
    s+=str(i)+","
    for x in range(n):
        i=0
        k=a
        for x in range(9):
            a+=k
        while a>=b:
            a-=b
            i+=1
        s+=str(i)
        if a==0:
            break
    print(s)
else:
    print("0 ga bo'lish mumkin emas!!!")