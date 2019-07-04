stuff={'name':'zed','age':24,'height':6*12+2}
print(stuff['name'])
print(stuff['age'])
print(stuff['height'])

#a=(stuff['height'])
#print(int(a))

stuff['city']='wuhan'
stuff[1]='wow'
stuff[2]='neate'
print(stuff)

del stuff[1]
del stuff[2]
del stuff['city']
print(stuff)