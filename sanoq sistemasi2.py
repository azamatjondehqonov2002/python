
def onlik(n,a):
    s=0
    k=True
    n=str(n)
    for i in range(n.__len__()):
        if ord(n[i]) >=48 and ord(n[i])<=57:
            if int(n[i])>=a:
                k=False
            else:
                s+=int(n[i])*(int(a)**(n.__len__() - i-1))
             
        elif ord(n[i])>=65 and ord(n[i])<=90:
            if ord(n[i])>=a+55:
                k=False
            else:
                s+=(ord(n[i])-55)*(a**(n.__len__() - i-1))
    
    if k:
        return s
    else:
        print("Siz kiritgan son ushbu sanoq sistemasiga tegishli emas!!!")

def otkazish(n,b):
    s=""
    n=int(n)
    while n!=0:
        if n%b<10:
            s=str(n%b)+s
            n//=b
        else:
            s=chr(n%b+55)+s
            n//=b
    
    return s

k = True
a=int(input("Qaysi sanoq sistemasida kiritmoqdasiz? \na = "))
n=input("Sonni kiriting: \nn = ")
b=int(input("Qaysi sanoq sistemasiga o'tkazmoqchisiz? \nb = "))


if a!=10:
    n =onlik(n,a)

if b!=10:
    n=otkazish(n,b)

print(n)