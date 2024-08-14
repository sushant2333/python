from collections import defaultdict

n,m = map(int,input("enter two number").split())

a = [input().strip() for _ in range(n)]
b = [input().strip() for _ in range(m)]

d = defaultdict(list)

for i in range(n):
    d[a[i]].append(i+1)

for word in b:
    if word in d:
        print(' '.join(map(str,d[word])))
    else:
        print(-1)