try:
    x=int(input('type the 1st number'))
    y=int(input('type the 2nd number'))
    z=input('type your desired operator(+,-,*,/)')

    if z=='+':
        print (x+y)
    elif z=='-':
        print (x-y)
    elif z=='*':
        print (x*y)
    elif z=='/':
        print (x/y)
    else:
        print ('!!! type the correct operator !!!')

except:
    print('type number only')