from sys import argv

script,input_file=argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)   ##把光标移动到文件的0字节


def print_a_line(line_count,f):
    print(line_count,f.readline(),end='')

current_file=open(input_file)

print('first let us print the file :\n')

print_all(current_file)

print('now let us rewind ,kind of like a tape ')
rewind(current_file) #这里一个该是把光标移到第一行

print(' let us print three lines:')
'''

current_line=1
print_a_line(current_line,current_file )#没有在这个位置加end='' 会使得函数误以为有三个参数而报错

current_line=current_line+1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)
'''
#用循环结构来写
for current_line in range (1,4):
    print_a_line(current_line, current_file)
    current_line +=1

