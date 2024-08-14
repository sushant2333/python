import abc
class student:
    
    @abc.abstractmethod
    def student_Detail(self):
        pass
    
    @abc.abstractmethod
    def student_marks(self):
        pass
    
    @abc.abstractmethod
    def student_assignment(Self):
        pass
    
class stu_detail(student):
    
    def student_Detail(self):
        print("this is to display student display")
        
    def student_marks(self):
        print("this is to display student marks ")
        
sd = stu_detail()
sd.student_assignment()
    