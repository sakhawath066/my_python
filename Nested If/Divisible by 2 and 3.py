## Let’s write a Python program to check whether a number is divisible by 2 and 3

x=int(input('Enter the number: '))

if x%2==0:
    print('it is divisible by 2')
    if x%3==0:
        print('it is also divisible by 3')
    else:
        print('it is divisible by 2 but not 3')
else:
    print('it is not divisible by any number')
