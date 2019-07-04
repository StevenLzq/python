print('how old are you ?',end='')
age=int(input())
print('how tall are you?',end='')#往末尾放一个空字符，这样print不会再加换行符
height=int(input())
print('how weight are you?',end='')
weight=input()
print("so,you are {} years old,{} tall and {} heavy.".format(age,height,weight))