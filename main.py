class patient:
    name=""
    address=""
    phone=""
    def add(self,name,address,phone):
        self.name=name
        self.address=address
        self.phone=phone
    def update(self,name,add,ph):
        self.name=name
        self.address=add
        self.phone=ph
    def delete(self):
        self.name=""
        self.address=""
        self.phone=""
def menu():
    print("Choose from the menu below :")
    print("1. For search")
    print("2. Update")
    print("3. Inserting new record")
    ch=input("Enter your choice")
gg=[]
def search(name=""):
    for i in range(1,gg.length()):
        if(i.name==name):
            print("Name is:"+i.name)
            print("Name is:"+i.address)
            print("Name is:"+i.phone)

if(ch=="1"):
    okk=input("Enter name to search: ")
    search(okk)
if(ch=="2"):
    okk=input("Enter name to update: ")
if(ch=="3"):
    while(True):
        name=input("enter name of patient: ")
        address=input("enter address of patient: ")
        phone=input("enter phone no of patient: ")
        ok=input("Do you want to add more records")
        if(ok=="no"):
            obj=patient()
            obj.add(name,address,phone)
            print("Record added \n")
            print("Name is:"+obj.name)
            print("Name is:"+obj.address)
            print("Name is:"+obj.phone)
            gg.append(obj)
            break
        if(ok=="yes"):
            obj=patient()
            obj.add(name,address,phone)
            print("Record added \n")
            print("Name is:"+obj.name)
            print("Name is:"+obj.address)
            print("Name is:"+obj.phone)
            gg.append(obj)
