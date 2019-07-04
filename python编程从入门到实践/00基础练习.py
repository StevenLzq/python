# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 18:36:52 2018

@author: 堪培拉的小熊熊~
"""
s='albert einstein '
t='once said'
r='"A person who never made a mistake never tried anything"'
print(s.title() +t+','+r)


#去空格
a=' huang pingping '
b=a.strip()
c=b.lstrip()
print(b,c)

#列表
name=['huang','li','zhang']
print(name[1].title()+':i love you')
print(name[0].title()+'你好吗？')
print(name[-1].title()+'吃饭了吗？')

name.append('zhao')
print(name)
name.insert(0,'wang')
print(name)
del name[3]
print(name)
name_poped=name.pop()
print(name)
print(name_poped)
named_poped=name.pop(0)
print(name)
print(named_poped)
name_removed='li'
name.remove(name_removed)
print(name)
name.insert(0,'liu')
print(name)

