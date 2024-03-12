try:
    a = int(input('enter number: '))

    if a>50:
        print('large')
    elif a==50:
        print('equal')
    else:
        print('small')

except:
    print('enter number values only')