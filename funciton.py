def test1():
    print('this is my first function')

def test2():
    return 'this is my first return'

def test3():
    return 1,2,'sushant',5.6

def test4():
    a=5+6/7
    return a

def test5(a,b,c):
    d = a+b/c
    return d

def test6(a,b):
    return a+b

def test7(a):
    """this is a function to extract integer from a list"""
    l1=[]
    for i in a:
        if type(i) == int:
            l1.append(i)
    return l1

def test8(*args):  # args can be replaced with any other name main work is of *
    return args

def test9(*args,a):
    return args,a

def test10(c,d,a=24,b=34):
    return a,b,c,d

def test11(**args):
    return args

# test1()
# print(test2()+" sushant")
# a,b,c,d = test3()
# print(a,b,c,d)
# print(test4())
# print(test5(2,5,8))
# print(test6('sudh','kumar'))

# l = [1,2,3,4,"sudh","kumar",[1,2,3,4],5]
# print(test7(l))

# print(test8(1,2,4,7.8,'sushant'))

# print(test9())
# print(test9(1,2,3,4,a=34))

# print(test10(3,4))

# print(type(test11()))
# print(test11(a=[12,34,45],b=56,c={3,4,5}))