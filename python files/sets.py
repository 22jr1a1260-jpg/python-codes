'''
s = {1,4,60,"veera",5,9}
s1 = {4,50,"geetha",7,8}
set = s.union(s1)
print(set)
'''
s = {1,2,3,3,5,6}
s1 = {4,5,5,9,60}
#set = s.union(s1)
#set = s.intersection(s1)
set = s.difference(s1)
#set = s.symmetric_difference(s1)
print(set)