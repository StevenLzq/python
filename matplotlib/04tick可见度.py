import numpy as np
import  pandas as pd
import matplotlib.pyplot as  plt


x=np.linspace(-3,3,50)
y=0.1*x

plt.figure()
plt.plot(x,y,linewidth=10,zorder=1)
plt.ylim(-2,2)
ax=plt.gca()
ax.spines['right'].set_color('none')#设置为不可见
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))#设置图的原点
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))#设置原点

"""在上面的过程会有线条覆盖住坐标轴熟知的情况"""

for label in ax.get_xticklabels() + ax.get_yticklabels():#在plt.plot()要加入zorder参数
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white', edgecolor='none', alpha=0.8, zorder=2))



plt.show()