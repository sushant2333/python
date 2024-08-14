import time

def time_test(func):
    def timer_test_inner():
        start = time.time()
        func()
        end = time.time()
        print(end-start)
    return timer_test_inner

def deco(func):
    def message():
        print("start")
        func()
        print("end")
    return message

@deco
def p():
    print(6+7)

# p()

@time_test
def test3():
    for i in range(1,100000):
        pass
    
test3()