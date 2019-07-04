import matplotlib.pyplot as plt
import numpy as np
"""x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2
plt.figure()
plt.plot(x,y1)

plt.figure(num=3,figsize=(8,5))
# plt.figure()
plt.plot(x,y2)
#设置颜色，线宽，线型
plt.plot(x,y1,color='red',linewidth=10.0,linestyle="--")
plt.xlim((-1,2))#取值范围
plt.ylim((-2,3))
plt.xlabel('I an X')#坐标轴名称
plt.ylabel('I am Y')
new_tick=np.linspace(-1,2,5)
print(new_tick)
plt.xticks(new_tick)#这个应该是刻度
# plt.yticks([-2,-1.8,-1,1.22,3],
#            ['really bad','bad','normal','good','really good'])#在轴上添加文字刻度
plt.yticks([-2,-1.8,-1,1.22,3],
            [r'$really\ bad$',r'$bad$',r'$normal$',r'$good$',r'$really\ good$'])#在轴上添加文字刻度

plt.show()
"""

####坐标轴设置2
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2
plt.figure()
plt.plot(x,y1)

plt.figure(num=3,figsize=(8,5))
# plt.figure()
plt.plot(x,y2)
"""设置颜色，线宽，线型"""
plt.plot(x,y1,color='red',linewidth=10.0,linestyle="--")
plt.xlim((-1,2))#取值范围
plt.ylim((-2,3))
plt.xlabel('I an X')#坐标轴名称
plt.ylabel('I am Y')
new_tick=np.linspace(-1,2,5)
print(new_tick)
plt.xticks(new_tick)#这个应该是刻度
plt.yticks([-2,-1.8,-1,1.22,3],
           ['really bad','bad','normal','good','really good'])#在轴上添加文字刻度

ax=plt.gca()
ax.spines['right'].set_color('none')#把右侧的轴设置为不可见
ax.spines['top'].set_color('none')#把顶部的轴设置为不可见
ax.xaxis.set_ticks_position('bottom')#把底部的轴代替xaxis
ax.yaxis.set_ticks_position('left')#把左侧的轴来代替yaxis
ax.spines['bottom'].set_position(('data',-1))#设置坐标轴位置
ax.spines['left'].set_position(('data',0))
plt.show()