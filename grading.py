try:   
    mark=int(input("Enter your marks: "))

    if mark<25:
        print('F')
    elif 45>mark>=25:
        print('E')
    elif 50>mark>=45:
        print('D')
    elif 60>mark>=50:
        print('C')
    elif 80>mark>=60:
        print('B')
    elif mark>=80:
        print('A')
    else:
        print("wrong input")
except:
    print('Enter number only')