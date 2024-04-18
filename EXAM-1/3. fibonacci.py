a = int(input('Enter the limit: '))
num1 = 0
num2 = 1
print ('Fibonacci series: ')

for z in range (0,a):
    if z<=1:
        num3 = z
    else:
        num3 = num1 + num2
        num1 = num2
        num2 = num3
    print(num3, end='')
