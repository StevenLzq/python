from sys import argv
script,filename=argv #写入参数数量和名称
txt=open(filename)  #打开文件

print('here is your file{}'.format(filename)) #用槽功能把文件名填充到前面
print(txt.read())#在读取内容之前要open一下
txt.close()
print('type the file name again:')
file_again=input('>') #再次运行一遍但是需要重新输入参数即文件名
txt_again=open(file_again)
print(txt_again.read())
txt.close()