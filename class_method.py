class student:
    
    mobile_number = 8862913318
    
    def __init__(self,name,email):
        self.name = name
        self.email = email
        
    @classmethod
    def change_number(cls,mobile):
        student.mobile_number=mobile
        
    @classmethod
    def details(cls, name, email):
        return cls(name,email)
        
    def getdetails(self):
        print(self.name,self.email,student.mobile_number)
        
def roll(cls,n):
    print("your roll is :",n)
        
        
# s1 = student.details("sushant","sush@gmail.com")

# print(s1.name)
# print(s1.email)
# s1.getdetails()
# print(student.mobile_number)

s2 = student.details("sushant","sush@gmail.com")

print(s2.name)
print(s2.email)
print(student.mobile_number)
s2.getdetails()
student.change_number(45)
s2.getdetails()
print(s2.mobile_number)

student.roll = classmethod(roll)
student.roll(1)

del student.change_number
# student.change_number(4)

delattr(student, "details")  # pass class name and function to be deleted as string
# student.details()


