n = int(input().strip())

l = [input().strip() for _ in range(n)]

d={}

for i in l:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i] = 1
        
print(len(d))
for k,v in d.items():
    print(v,end=' ')