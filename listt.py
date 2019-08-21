l1=[1,3,6,78,35,55]
l2=[12,24,35,24,88,120,155]
l1.extend(l2)
l1.sort()
print(l1)
l4=[]
d=len(l1)
for i in range(0,len(l1)):
    #c=l1.count(l1[i])
    if(i==d-1):
        break
    if(l1[i]==l1[i+1]):
        l4.append(l1[i])
print(l4)
        
        
               
               
