def fib(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b = b,a+b

def fib1():
    a,b=0,1
    while True:
        yield a
        a,b = b,a+b

# for i in fib(10):
    # print(i)

# for i in fib1(10):
#     print(i)

# l =[3,5,4,6]
# itr = iter(l)
# d={3:'sushant'}
# itr1=iter(d)
# for i in range(len(l)):
#     print(next(itr))
# print(next(itr,"we have reached the end of list"))

# while True:
#     item = next(itr,"end")
#     if item=='end':
#         break;
#     print(item)
# print(type(itr))
# print(type(itr1))
# i= next(itr)
# print(type(i))

# f = fib1()
# print(type(f))
# for i in range(10):
#     print(next(f))