import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2
plt.figure()
plt.plot(x,y1,label='down')

plt.figure(num=3,figsize=(8,5))
# plt.figure()

plt.xlim((-1,2))#取值范围
plt.ylim((-2,3))
plt.xlabel('I an X')#坐标轴名称
plt.ylabel('I am Y')
new_tick=np.linspace(-1,2,5)
print(new_tick)
plt.xticks(new_tick)#这个应该是刻度
plt.yticks([-2,-1.8,-1,1.22,3],
           ['really bad','bad','normal','good','really good'])#在轴上添加文字刻度

l1,=plt.plot(x,y2)#后面的逗号不可省略  是省略掉的一个参数
"""设置颜色，线宽，线型"""
l2,=plt.plot(x,y1,color='red',linewidth=10.0,linestyle="--",)
plt.legend(handles=[l1,l2,],prop={'family':'SimHei','size':15},labels=['aaa','bbb'],loc='upper right')
"""loc =left right lower upper"""


plt.show()