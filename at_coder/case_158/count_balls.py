import sys

n,a,b=map(int,input().split())

if a == 0:
    print(0)
    sys.exit()

lst = []
is_blue = True
count = 0
for i in range(n):
    if is_blue:
        lst.append('b')
        count += 1
        if count == a:
            is_blue = False
            count = 0
    else:
        lst.append('r')
        count += 1
        if count == b:
            is_blue = True
            count = 0

result = list(filter(lambda x:x == 'b', lst))
print(len(result))