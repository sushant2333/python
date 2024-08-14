from collections import deque

def isnum(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

n = int(input().strip())

d = deque()

for i in range(n):
    request = input().strip().split()
    if isnum(request[-1]):
        