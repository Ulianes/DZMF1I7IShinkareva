import math
t=float(input('Введите t:'))
a=(t-2)
b=(4*t-1)
c=(3*t-5)
if a==0:
    x=c/b
    print('x=', x)
else:
    D=b**2-4*a*c
    print('D:',D)
    print('a:',a)
    print('b:',b)
    print('c:',c)
    if D>=0:
        x1=(-b+math.sqrt(D))/(2*a)
        x2=(-b-math.sqrt(D))/(2*a)
        print('x1=',x1,'x2=',x2)
    else:
        print('D<=0')