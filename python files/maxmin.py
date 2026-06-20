l = [15,2,6,25,10]
max = l[0]
min = l[0]
for i in l:
    if i > max:
        max = i
    if i < min:
        min = i
print(max,min)