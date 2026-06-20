a = int(input("Give a="))
b = int(input("Give b="))  
c = int(input("Give c="))
d = (b**2) - 4*a*c
r1 = (-b + (d**(0.5)))/2*a
r2 = (-b - (d**(0.5)))/2*a
print("Roots:",r1,r2)
