a=input("enter")
b=input("enter")
c=input("enter")
file=open("1.txt","w")
file.write(a)
file.write(b)
file.write(c)
file=open("1.txt","r")
print(file.read())
#برنامه برای نوشتن استرینگ های ورودی
