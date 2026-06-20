'''
for i in "pythonlife":
    if i=='o':
        continue
    print(i)

for i in range(0,10):
    if i == 5:
        continue
    print(i)
'''
sum = 0 # intialize extra variable
n = int(input("N = "))
for i in range(1,n+1):
    sum += i #sum variable for store i value and make it sum
   #print(sum)declare here to get iteration 
print("sum of first 5 natural numbers",sum) # declare here to get last value
    
    