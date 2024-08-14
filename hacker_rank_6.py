if __name__ == '__main__':
    l = []
    s=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l1 = [name,score]
        l.append(l1)
        s.append(score)
    s = set(sorted(s))
    s=list(s)
    sl = s[1]
    names = sorted([x[0] for x in l if x[1]==sl])
    for name in names:
        print(name)