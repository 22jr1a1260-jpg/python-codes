year = int(input("Enter year: "))
leap = False
if year%100 == 0 and year%400 != 0:
    leap = False
    print(year,"leap year")
elif year%4 == 0:
    leap = True
    print(year,"leap year")
else:
    print(year,"not a leap year") 