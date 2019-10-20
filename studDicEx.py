class StudentNotFoundException(Exception):
	pass
class main():
	dic={}
	def add(self):
		l=[]
		name=input("enter name of student ")
		l.append(name)
		age=(int)(input("enter age: "))
		l.append(age)
		course=input("enter couse :")
		l.append(course)
		sem=(int)(input("enter semester: "))
		l.append(sem)
		marks=(int)(input("enter marks: "))
		l.append(marks)
		self.dic[name]=l
	def search(self):
		nm=input("enter name of student for search ")
		if(nm==""):
			exit
		k=self.dic.get(nm)
		if(k==None):
			try:
				oo="student not found"
				raise StudentNotFoundException(oo)
			except StudentNotFoundException as ss:
				print(ss)
		else:
			print(k)
			exit
ll=[]
while(True):
	print("choose from the menu")
	print("1. search student")
	print("2. enter new entry")
	ch=input("enter your choice:")
	mm=main()
	if(ch=="2"):
		mm.add()
	elif(ch=="1"):
		ll.append(mm)
		for i in range(0,len(ll)):
			ll[i].search()
	
	ok=input("press 9 to exit")
	if(ok=="9"):
		break



