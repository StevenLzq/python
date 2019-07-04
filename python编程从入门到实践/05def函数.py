'''

def get_users_name(first_name,last_name):
    full_name=first_name+last_name
    return full_name.title()
while True:
    print('please tell me your name: ')
    print("enter 'q'to quit at any time")
    f_name=input('first_name')
    if f_name=='q':
        break
    l_name=input('last_name')
    if l_name=='q':
        break
    users_name=get_users_name(f_name,l_name)
    print('hello, '+users_name+'!')


   #################################################################
def greet_user(names):
    for name in names:
        msg=print('hello'+name.title()+'!')

usernames=['li','huang','zhao']
greet_user(usernames)


##########################################################
def print_models(need_prints,completed_prints):
    while need_prints:
        current_print=need_prints.pop()
        print('printing:\n'+current_print)
        completed_prints.append(current_print)
def show_completed(completed_prints):
    print("the following have been printed:")
    for model in completed_prints:
        print(model)

needed_prints=['ipohone case','robor pendant','list']
completed_prints=[]

print_models(needed_prints,completed_prints)
show_completed(completed_prints)



#####################################################################

def make_pizza(*toppings):
    print('\nmakeing a pizza with the following toppings')
    for topping in toppings:
        print('-'+topping)

make_pizza('pepperoin')
make_pizza('mushrooms','green peppers','extra cheese')




##########################################################################

def make_pizza(size,*toppings):
    print('\n make a '+str(size)+' inch pizza with the folowing toppings:')
    for topping in toppings:
        print("-"+topping)
make_pizza(10,'pepperoin')
make_pizza(16,'mushrooms','grren peppers','extra cheese')


#############################################################################

def build_profile(first_,last,**user_info):
    profile={}
    profile['forst_name']=first_
    profile['last_name']=last
    for key ,value in user_info.items():#item()方法把字典中每对key和value组成一个元组
        profile[key]=value
    return profile
user_profile=build_profile('albert','einsten',location='princeton',field='physics')
print(user_profile)




############################################8-12######################################
def make_sandwich(*toppings):
    print('\nyou order a sandwich with the following topping :')
    for topping in toppings:
        print(topping)
topping1=('peppers','meat')
topping2=('cheese','mushrooms')
make_sandwich(topping1)
make_sandwich(topping2)



########################################8-13#########################################
def build_profile(first_,last,**user_info):
    profile={}
    profile['forst_name']=first_
    profile['last_name']=last
    for key ,value in user_info.items():#item()方法把字典中每对key和value组成一个元组
        profile[key]=value
    return profile
user_profile=build_profile('albert','einsten',location='princeton',field='physics')
my_profile=build_profile('li','steven',location='wihan',age='24',major='enginery')
print(user_profile)
print(my_profile)
'''


####################################################################################
