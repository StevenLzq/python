# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 20:00:04 2018

@author: 堪培拉的小熊熊~
"""

wendu=input('请输入温度')
if wendu[-1] in('c','C'):
    F=1.8*eval(wendu[0:-1])+32
    print("转化后温度为{:.2f}F".format(F))  
    #{}槽功能{:.2f}表示将后面的数值取小数点后两位填充到该位置
elif wendu[-1] in ('f','F'):
    C=(eval(wendu[0:-1])-32)/1.8
    print("转化后温度为{:.2f}C".format(C))
else:    
    print('输入错误')     