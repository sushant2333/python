class test:
    
    def test_meth(self):
        return "this is my first class "
    
class child_test(test):
    pass

child_obj = child_test()
print(child_obj.test_meth())


    