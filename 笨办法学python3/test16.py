from sys import argv

script ,filename=argv

print ('we are going to erase{}'.format(filename))

print('if you dont want it ,hit CTRL-C(^C)')

print('if you want it hit RETURN')

input("?")
print('opening the file...')
target=open(filename,'w')

print('truncating the file. goodbye')

target.truncate()

print('now you should write three lines')

line1=input('line1:')
line2=input('line2:')
line3=input('line3:')

print(' i am going to write these to the file')
'''
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')
print('finally we check and close it')
target.clode()
'''

target.write(line1 +'\n'+line2+'\n'+line3)
print ('finally we check and close it ')
target.close()