#s - sekund, m - minut, h - soat, d - kun
a= int(input("Soniyani kiriting "))
s=a%60
a=a//60
m=a%60
a=a//60
h=a%24
a=a//24
d=a
satr= "Berilgan vaqtda "
if d!=0:
    satr+=str(d) + " kun "
if h!=0:
    satr+= str(h) + " soat "
if m!=0:
    satr+=str(m) + " minut "
if s !=0:
    satr+= str(s) + "sekund "
satr+="bor."
print (satr)