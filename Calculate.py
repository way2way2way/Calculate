import sys
a = float(input('number?:'))
b = int(input('1(+)2(-)3(*)4(/)?:'))
if b>4 or b<1:
    print(f'error404 {b} is not found')
    sys.exit()
c = float(input('number?:'))
if b==1:
    result = a + c
    print(result)
    print(f'{a} + {c} = {result}')
elif b==2:
    result = a - c
    print(result)
    print(f'{a} - {c} = {result}')
elif b==3:
    result = a * c
    print(result)
    print(f'{a} * {c} = {result}')
elif b==4:
    if c==0:
        print(f"error {a} / {c} is Can't calculate")
        sys.exit()
    result = a / c
    print(result)
    print(f'{a} / {c} = {result}')
