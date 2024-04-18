def calculator(a, b, c):
    if c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "*":
        print(a * b)

user1 = int(input())
user2 = int(input())
user3 = input()
calculator(user1, user2, user3)
