#Tuple
atuple = ('test', 20, 30,40, True, 50)
print(atuple[2])
g=('sakhawath', )
atuple+=g
print(atuple)


#Set
aset = {11,92,32,64,58,46,370,78,19}
aset.add (666)
aset.remove(32)
print(aset)

a = {1,2,3,4,5,6,7}
b = {5,6,7,8,9,10,11}
print (a|b)
print (a&b)


#Dictionary
adict = {

    'name' : 'sakhawath',
    'age' : 18,
    'town' : 'Dhaka',
    'is_married' : True,
    'alist' : [1,2,3,4,5],
}

adict['name'] = 'ttt'
adict.update({'id' : 1})
print(adict)