# store and print the length 
# of each word in a list

names = ['basic',
         'coding',
         'subscribe']

l = [len(i) for i in names]
print(l)

d = {i:len(i) for i in names}
print(d)