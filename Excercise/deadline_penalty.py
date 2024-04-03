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

Dis1 = tuple((b[-1], a[0],))
Dis2 = tuple((b[-2], a[1],))
Dis3 = tuple((b[-3], a[2],))

print(Dis1, Dis2, Dis3)

