a=input()
b=int(a)
c=0
d=0
while a != '-1':
    if b>c and b>10 and b<90:
        d=c
        c=b
        print('c= ',c)
    if b!=c and b>10 and b<90 and b > d:
        d=b
        print('d= ',d)
    
    a=input()
    b=int(a)

print(c,'',d)