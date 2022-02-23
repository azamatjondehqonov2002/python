a=float(input("a = "))
b=float(input("b = "))
c=float(input("c = "))

if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
    print("True")
else:
    print("Falce")