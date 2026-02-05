import sys
a = float(input('number?:'))
b = int(input('1(+)2(-)3(*)4(/)?:'))
if b>4 or b<1:
    print(f'error404 {b} is not found')
    sys.exit()
c = float(input('number?:'))
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
    if c==0:
        print(f"error {a} / {c} is Can't calculate")
        sys.exit()
    print(a/c)
    print(f'{a} / {c} = {a / c}')
