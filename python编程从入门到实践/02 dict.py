dict={'huangpp':'5','liwei':'2','pingbao':'0'}
print("huangpp's favorate num is" + ' '+dict['huangpp'])
del dict['liwei']
for key ,value in dict.items():
    print('\nkey:'+key)
    print('\nvalue:'+value)
    print(key+"'s favorate num is "+value)

for name in sorted(dict.keys()):
    print(name)
for num in set(dict.values()):
    print(num)