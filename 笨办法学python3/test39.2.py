'''
states={
    'oregon':'OR',
    'florida':'FL',
    'california':'CA',
    'michigan':'MI'
}

cities={
    'CA':'san francisco',
    'MI':'detroit',
    'FL':'jacksonville',

}

cities['NY']='newyork'
cities['OR']='portland'

print('-'*10)
print('NY state has :',cities['NY'])
print('OR state has :',cities['OR'])

print('-'*10)
print('michigan\' abbreviation is ',states['michigan'])

print('-'*10)
print('michigan has:',cities[states['michigan']])
print('florida has :',cities[states['florida']])

#print every state abbreviation
print('-'*10)
for state,abbrev in list(states.items()):
    print(format,'{state} is abbreviated {abbrev}')

#print every city in state

print('-'*10)
for abbrev,city in list(cities.items()):
    print(format,'{abbrev} has city {city}')

#now do both on the same time
print('-'*10)
for state,abbrev in list(states.items()):
    print(format,'{state} state is abbreviated {abbrev}')
    print(format,'and has city {cities[abbrev]}')

print('-'*10)
state=states.get('texas')
if not state:
    print('sorry no texas')

city=cities.get('TX')
print(format,'the city for thr state \'TX\' is:{city}')

'''
# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': "NY",
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print ('-' * 10)
print ("NY State has: ", cities['NY'])
print ("OR State has: ", cities['OR'])

# print some states
print ('-' * 10)
print ("Michigan's abbreviation is: ",states['Michigan'])
print ("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print ('-'* 10)
print ("Michigan has: ", cities[states['Michigan']])
print ("Florida has: ", cities[states['Florida']])
# 这里 states['Michigan'] = MI，而cities['MI'] = detroit
# print every state abbreviation
print( '-' * 10)
for state, abbrev in states.items():
    print ("%s is abbreviated %s" % (state, abbrev))

# print every city in state
print ('-' * 10)
for abbrev, city in cities. items():
    print( "%s has the city %s" % (abbrev, city))
# items 是遍历字典内所有元素
# now do both at the same time
print ('-' * 10)
for state, abbrev in states.items():
    print( "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev]))


print ('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas', None)
# get 作用与 in 类似，都是判断是否存在，如果存在，则正常打印，如果不存在，返回指定值
if not state:
    print (*"Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print("the city for thr state \'TX\' is:{}".format(city))
#print ("The city for the state 'mmmmTX' is: %s" % city)