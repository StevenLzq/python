#############################列表中存储字典#################################
aliens=[]
for alien_num in range (30):
    new_alien={'color':'green','point':5,'speed':'slow'}
    aliens.append(new_alien)


for alien in aliens[0:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['point']=10
    elif alien['color']=='yellow':
        alien['color']='red'
        alien['speed']='fast'
        alien['point']=15


for alien in aliens[0:5]:

    print(alien)
print('...')

################################字典中存储列表############################################
pizza={'crust':'thick','topping':['mushrooms','extra chesse']}
print('you order a'+pizza['crust']+'-crust pizza'+
      'with the following topping:')
for topping in pizza['topping']:
    print(topping)


favorate_languages={
    'jen':['python','c'],
    'lisa':['rby'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
}
for name ,languages in favorate_languages.items():
    print ('\n'+name.title()+"'s favorate languages are:")
    for language in languages:
        print('\t'+language.title())


####################################################################################
