#count numbers in given list
#inp = input().split(",")
#l = [int(items) for items in inp]
#l = [int(items) for items in input().split(',')] 
l = [1,2,3,2,1,4,2,5] 
l = [int(i) for i in l] 
n = int(input())
cnt = 0
for i in l:
    if i == n:
        cnt+=1
print(cnt)
