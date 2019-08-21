a=(int)(input("enter a"))
b=(int)(input("enter b"))
c=[]
d=[]
def loopp(a,b):
    k=0
    while(k!=9):
        c.append(a)
        d.append(b)
        b=b+1
        a=a-1
        k=k+1
    return a+b
print("sum of the numbers after substraction",loopp(a,b))
print("sum of individual A ",sum(c))
print("sum of individual B ",sum(d))