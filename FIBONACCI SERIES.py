x=0
y=1
z=x+y
n=int(input("enter the limit:-"))
print("fibonacci series:")
print(x,y,end=" ")
while  z<=n:
    print (z,end=" ")
    x=y
    y=z
    z=x+y
