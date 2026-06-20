num1 = int(input("Enter a value:"))
num2 = int(input("Enter another value:"))
opr = input("give operator: ")
if opr == "+":
    print(f"Sum of two nums: {num1+num2}")
elif opr == "-":
    print(f"Sub of two nums: {num1-num2}")
elif opr == "*":
    print(f"mul of two nums: {num1*num2}")
elif opr == "/":
    print(f"Div of two nums: {num1/num2}")
else:
    print("Not valid")

