a=float(input("a = "))
b=float(input("b = "))
c=float(input("c = "))
n=0
p=0
nol=0
if a>0:
    p+=1
elif a==0:
    nol+=1
else:
    n+=1

if b>0:
    p+=1
elif a==0:
    nol+=1
else:
    n+=1

if c>0:
    p+=1
elif a==0:
    nol+=1
else:
    n+=1

print("Musbatlar ", p, " ta, nol ", nol, " ta, manfiy", p, " ta")