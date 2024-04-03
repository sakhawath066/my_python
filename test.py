a = [['naim', 50], ['sadi', 12], ['Rafi', 48], ['Ritu', 80], ['Basi', 10]]
x = []
y = []
output = []

for i in a:
    x.append(i[-1])

x.sort()
for i in a:
    for j in x[:2]:
        if j == i[-1]:
            y.append(i)
y.sort()
for i in y:
    output.append(i[0])
y.sort()
print(output)

