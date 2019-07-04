from sys import argv
from os.path import exists

script,from_file,to_file=argv  #选择好一点的变量名

print('copy from {} to {}'.format(from_file,to_file))

in_file=open(from_file)
indata=in_file.read()

print('the input file is{} bytes long'.format(len(indata)))
print('does the to_file exist?{}'.format(exists(to_file)))
print ('ready hit RETURN  to continue ')
input()

out_file=open(to_file,'w')
out_file.write(indata)


print('alright all done')
out_file.close()
in_file.close()