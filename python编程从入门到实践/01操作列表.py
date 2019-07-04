# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 18:55:21 2018

@author: 堪培拉的小熊熊~
"""

squares=[value**2 for value in range(1,10) ]
print (squares)
num=[a*2-1 for a in range(1,11)]
print(num)
c=[a for a in range(3,31,3)]
d=['as','qw','qwe','df','gh','ght']
print ('the first three items in this list are: %s'%d[0:3])

ls=('jiaozi','mantou','bin','dangao','mianbao')
for i in ls:
    print(i)
ls=('baozi','youtiao','bin','dangao','mianbao')
for i in ls:
    print(i)
    
    

    