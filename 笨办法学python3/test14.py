from sys import argv

script,user_name=argv
prompt="user_>"

print('hi {},i am the{} script'.format(user_name,script))

print('i would like to ask you some questiuons?')

print('do you like me {}'.format(user_name))

likes=input(prompt)

print('where do you live {}'.format(user_name))
lives=input(prompt)#这里用prompt作为提示输入

print('what kind of computer do you hace?')
computer=input(prompt)

print('''
so  you said {} about liking me.
you live in {} nnot sure where that is.
and you hace a{} computer. nice!
'''.format(likes,lives,computer))