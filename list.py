alist=[18,20.00,15,2,4,6,8,10]
print(alist)
print(alist[:5])
print(alist[2:5])
print(alist[6])
print(alist[1],alist[3],alist[4])
print(max(alist))
print(min(alist))
print(sum(alist))
print(sorted(alist))
print(alist.index(15))
alist.append(30)
alist.insert(2,40)
alist.remove(8)
alist.pop()
alist.pop(1)
alist.reverse()
print(alist)