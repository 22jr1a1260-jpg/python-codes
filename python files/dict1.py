'''
my_dict = {}
name = input("name: ")
age = int(input("age: "))
city = input("city: ")
my_dict['name'] = name 
my_dict['age'] = age 
my_dict['city'] = city 
print(my_dict)
'''
my_dict = {
    "name" : "jhon",
    "age"  : 20,
    "city" : "new york"
}
#for i in my_dict.values():
    #print(i)
#print(my_dict)
print(my_dict.get("city"))
my_dict.update({"love":143})
print(my_dict)