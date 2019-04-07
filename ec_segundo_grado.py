a = float(input("ingresa a: "))
b = float(input("ingresa b: "))
c = float(input("ingresa c: "))

def resolvente(a,b,c):
	x1 = (-b + (b**2 - 4*a*c)**(1/2.0))/(2.0*a)
	x2 = (-b - (b**2 - 4*a*c)**(1/2.0))/(2.0*a)
	print(x1)
	print("\n")
	print(x2)

resolvente(a,b,c)

