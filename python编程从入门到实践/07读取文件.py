'''
with open ('pi_digits.txt')as file_object:

    content=file_object.read()

    print(content.rstrip())#read()到大文件末尾返回一个空字符，显示为一行，可用content.rstrip()删除空行


####################################################
file_name='pi_digits.txt'
with open(file_name)as file_object:
    lines=file_object.readlines()#把文件各行存储到一个列表中Readlines()从文件中读取各行

    for line in lines:
        print(line.rstrip())


########################################################################

file_name = 'pi_digits.txt'
with open(file_name)as file_object:
    lines = file_object.readlines()  # 把文件各行存储到一个列表中Readlines()从文件中读取各行
    pi_string=''
    for line in lines:
        pi_string +=line.strip()#strip 删掉左边 r right

print(pi_string[:30])
print(len(pi_string))

################################################################################
file_name='programing.txt'
with open(file_name,'w')as file_object:#'w'会清空之前的内容
    file_object.write('i love programing !')



file_name='programing.txt'
with open(file_name,'a')as file_object:#'a'不会覆盖之前的的内容而只是在后面添加
    file_object.write('\nMe too')


##################################################################
file_name='guest.txt'
s=input('hello,may i have y our name?')
with open(file_name,'a')as file_object:
    file_object.write(s)

####################################################################
import json
numbers=[2,3,5,7,11,13]
filename='numbers.json'
with open(filename,'w')as f_obj:
    json.dump(numbers,f_obj)


#################################################################
import json
file_name='numbers.json'
with open(file_name)as f_obj:
    numbers=json.load(f_obj)

print(numbers)

#####################################################################

import json
username=input('what is your name?')
filename='username.json'
with open(filename,'w')as f_obj:
    json.dump(username,f_obj)

print('we will remember your name,when you come back '+username.title())


########################################################################
import json
filename='username.json'
try:
    with open(filename)as f_obj:
        username=json.load(f_obj)
except FileNotFoundError:
    username=input('what is your name?')
    with open(filename,'w')as f_obj:
        json.dump(username,f_obj)
        print('we will remember you,when you come back '+username.title())
else:
    print('welcome back '+username.title())
'''
##############################################################################
import json

def get_sorted_username():
    filename='username.json'
    try:
        with open(filename)as f_obj:
            username=json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username=input('what is your name?')
    filename='username.json'
    with open (filename,'w')as f_obj:
        json.dump(username,f_obj)
    return username
def greet_user():
    username=get_sorted_username()
    if username:
        print('welcom back '+username.title())
    else:
        username=get_new_username()
        print('i will renmmeber you ,when you come back '+username.title())

greet_user()

