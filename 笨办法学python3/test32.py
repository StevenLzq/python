the_count=[1,2,3,4,5]
fruits=['apples','oranges','pears','apricots']
change=[1,'pennies',2,'dimes',3,'quartera']

for num in the_count:
    print('this is count {}'.format(num))
for fruit in fruits:
    print('here is the{}'.format(fruit))

for i in change:
    print('i get {}'.format(i))

element=[]

for i in range(1,6):
    print('add {} into element'.format(i))
    element.append(i)

for i in element:
    print('element is {}'.format(i))
print(element[0])