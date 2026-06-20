a = int(input("marks in math: "))
b = int(input("marks in science: "))
c = int(input("marks in english: "))
total_marks = a+b+c
avg = total_marks / 3
if avg > 90:
    print("Grade : S")
elif avg > 80:
    print("Grade : A")
elif avg > 70:
     print("Grade : B")
elif avg > 60:
    print("Grade : C ")
elif avg > 50:
    print("Grade : D ")
elif avg > 40:
    print("Grade : E")
elif avg < 40:
    print("Grade : F")
else:
    print("Not valid")
print("Total Marks:",total_marks)
print("Average Marks:",avg)



     
     
     
     
     
