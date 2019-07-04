ten_things='apples oranges crows telphones light sugar'
print('wait,there are not ten things in the list .let us fix it')
stuff=ten_things.split()
#print(stuff)

more_stuff=['day','night','song','frisbee','corn','banana','girl','boy']

while len(stuff)!=10:
    next_one=more_stuff.pop()
    print('adding:',next_one)
    stuff.append(next_one)
    print('there are {} items now'.format(len(stuff)))

print('there we go',stuff)

print ('let us do somthing with the stuff')
print(stuff[1])
#print(stuff.pop(1))
#pop.()默认是-1，是从列表里面取出
print(stuff[-1])
#print(stuff.pop())

print(stuff)
print(' '.join(stuff))
print(stuff)
print('#'.join(stuff[3:5]))
print(stuff)