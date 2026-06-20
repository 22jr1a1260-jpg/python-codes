s=open('demo.txt',mode='w+')
s.seek(0)
print(s.read())
s.write("iam not good at studies")

print(s.close())