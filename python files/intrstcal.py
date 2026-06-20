
p = int(input("Enter principle amount: "))
t = float(input("Enter period of time: "))
r = float(input("Enter Rate of interest: "))
amt = p * t * r/100
tol = p + amt

print("Interest = ",amt)
print("Total amount = ",tol)

