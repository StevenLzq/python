##########################int（)   input()######################################################
'''
height=input('how tall are you ,in inches?')
height=int(height)

if height>=36:
    print('\nyou are tall enough to ride!')
else:
    print("\nyou'll be able to ride when you are a little older.")
###########################################################################################




current_num=0
while current_num<=5:
    print(current_num)
    current_num+=1
############################################################
prompt='\ntell me something,and i wiil repest it back to you'
prompt+='\nenter quit to end this program\n'
message=""
while message !='quit':
    message=input(prompt)
    if message !='quit':

     print(message)
#################################################################
prompt='\ntell me something,and i wiil repest it back to you'
prompt+='\nenter quit to end this program\n'
message=""
active=True
while active:
    message=input(prompt)
    if message=='quit':
        active=False

    else:
        print(message)

#########################################################
prompt='\nplease enter the name of a city that you have visited'
prompt+="\n（enter 'quit' when you want to finish）"

while True:
    city=input(prompt)
    if city =='quit':
        break
    else:
        print("i'd love to go to"+city.title()+'!')
#############################################################
current_num=0
while current_num<=10:
    current_num+=1
    if current_num%2==1:
        continue#跳过下面程序直接跳到循环开始
    print(current_num)
###################################################


prompt='\nplease tell us what you want to add\n'

prompt+="\n(enter 'quit' to finish)"
while True:
    message=input(prompt)
    if message=='quit':
        break
    else:
        print('the '+str(message)+' have been added')



################################################################

unconfirmed_users=['alice','jian','maria']
confirmed_users=['lisa']

while unconfirmed_users
    current_user=unconfirmed_users.pop()
    print('verifying user:'+current_user.title())
    confirmed_users.append(current_user)
print('the following users have confirmed:')
for user in confirmed_users:
     print(user.title())

#####################################################################
pets= ['cat','dog','cat','rabbit','bird','pig']
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#####################################################################


responses={}
active=True

while active:
    name=input('\nwhat is  your name?')
    response=input('which mountain do yu like to climb?')
    responses[name]=response
    #responses={'name':''response'}这里只是把他们成对的存储到一起  并没有什么实际意义

    repeat=input('would you like anothoer person respond?(yes/no)')
    if  repeat =='no':
        active=False


print('\n---poll results----')
for name, response,in responses.items():
    print(name+' would like to climb '+response)
'''
##########################################################################################
responses={}
active=True
while active:
    name=input('\nwhat is your name?')
    response=input('if you could visit one place in the world,where would you go?')
    responses[name]=response
    repeat=input('would you like another person respond(yes/no)?')
    if repeat=='no':
        active=False
print('\n---poll results---')
for name, response in responses.items():
    print(name+' would like to go '+response)