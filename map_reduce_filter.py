# from functools import reduce

# map is used to map a function with a iterable  
# l = [2,3,4,5,6]
# def sq(x):
#     return x**2
# print(list(map(sq,l)))
# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9,10]
# def sum(l1,l2):
#     return l1+l2
# print(list(map(sum,l1,l2)))
# p='pwskills'
# print(list(map(lambda a : a.upper(),p)))

# third parameter cannot be taken because reduction is not possible all the time
# l = [1,2,33,4,5]
# print(reduce(lambda x,y:x+y,l))
# print(reduce(lambda x,y:x if x>y else y,l))

# l = [1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x : x%2==0,l)))
# print(list(filter(lambda x : x%2==1,l)))
# print(list(filter(lambda x : x%2==1,l)))