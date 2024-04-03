task = [(3, 100), (1, 300), (2, 200)]
a = []
b = []

for i in task:
    a.append(i[-1])
a = list(a)
a.sort()

for i in task:
    b.append(i[-2])
b = list(b)
b.sort()

Dis = tuple((b[-1], a[0], b[-2], a[1], b[-3], a[2]),)
print(Dis)
