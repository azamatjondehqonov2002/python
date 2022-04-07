#5-masala
#kattalari orasida a eng kichik, b o'rta, c eng katta
n=int(input())
if n<3:
    print("Siz kerakgidan kam son kirityapsiz")
else:
    a=float(input())
    b=float(input())
    c=float(input())
    if a>b:
        a,b=b,a
    if a>c:
        a,c=c,a
    if b>c:
        b,c=c,b
    for x in range(3,n):
        k = float(input())
        if k>a:
            if k>b:
                if k>c:
                    a,b,c=b,c,k
                else:
                    a,b,c=b,k,c
            else:
                a,b,c=k,b,c

print(a,b,c)