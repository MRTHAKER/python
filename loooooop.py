ll=[]
lll=[]
res=[]
while(True):
    c=(int)(input("enter elelemnt for first list"))
    ll.append(c)
    d=input("you want to add more elements ?")
    if(d=="no"):
        break

while(True):
    e=(int)(input("enter element for second list"))
    lll.append(e)
    f=input("you want to add more elements ?")
    if(f=="no"):
        break
print(ll)
print(lll)
gg=len(ll)+len(lll)
for i in range(0,max(len(ll),len(lll))):
             if(i<len(ll) and ll[i]%2==0):
                res.append(ll[i])
             if(i<len(lll) and lll[i]%2!=0):
                res.append(lll[i])

print(res)
