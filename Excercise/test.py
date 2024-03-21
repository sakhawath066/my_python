# Write a Python program to calculate the sum of three given numbers.
# If the values are equal, return three times their sum.

n1 = int(input('enter 1st number: '))
n2 = int(input('enter 2nd number: '))
n3 = int(input('enter 3rd number: '))
z = n1+n2+n3

if n1==n2==n3:
    print(z*3)
else:
    print(z)
