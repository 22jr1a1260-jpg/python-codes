a = input("enter 3 values: ")
x,y,z = a.split(",")
num1 = int(x)
num2 = int(y)
num3 = int(z)
if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num2)
elif num2 > num1:
    if num2 > num3:
        print(num2)
    else:
        print(num3) 
elif num3 > num1:
    if num3 > num2:
        print(num3)
    else:
        print(num2)   
