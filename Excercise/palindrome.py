x = int(input('enter your number: '))
y = str(x)
z = int(y[::-1])

if x == z:
    print('TRUE')
else:
    print('FALSE')
