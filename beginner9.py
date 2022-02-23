from math import sqrt
a = float(input("a = "))
b = float(input("b = "))
if a<0 or b<0:
    print("Siz manfiy son kiritdingiz. Sonlarni qaytadan kiriting!!!\n")
while a<0 or b<0:
    a = float(input("a = "))
    b = float(input("b = "))
    if a<0 or b<0:
        print("Siz manfiy son kiritdingiz. Sonlarni qaytadan kiriting!!!\n")

c = sqrt(a*b)
print("c = ",c)