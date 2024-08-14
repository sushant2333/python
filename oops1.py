class test:
    def welcome(self):
        print("welcome")
        
a = test()
# a.welcome()

class test2:
    def __init__(self,phone_number, email, id) : # instead of self we can use any variable
        self.phone1 = phone_number
        self.email1=email
        self.id1=id
        
    def student_detail(self):
        return self.phone1,self.email1,self.id1
    
rohan = test2(238428,"rohan@example.com",56)
print(rohan.student_detail())
print(rohan.email1)
