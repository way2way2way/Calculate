import sys
a = int(input('number?:'))
b = int(input('1(+)2(-)3(*)4(/)?:'))
if b>4 or b<1:
    print(f'error404 {b} is not found')
    sys.exit()
c = int(input('number?:'))
if b==1:
    print(a+c)
    print(f'{a} + {c} = {a + c}')
elif b==2:
    print(a-c)
    print(f'{a} - {c} = {a - c}')
elif b==3:
    print(a*c)
    print(f'{a} * {c} = {a * c}')
elif b==4:
    print(a/c)
    print(f'{a} / {c} = {a / c}')