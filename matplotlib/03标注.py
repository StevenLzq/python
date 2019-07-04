import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)
y=2*x+1
plt.figure(num=1,figsize=(8,5))
plt.plot(x,y,)
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(("data",0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

x0=1
y0=2*x0+1
plt.scatter(x0,y0,s=50,color='b')#标出一个点
plt.plot([x0,x0],[y0,0],'r--',lw=2.5)

plt.annotate(r'$2x+1=%s$'%y0,xy=(x0,y0),xycoords='data',
             xytext=(+30,-30),textcoords='offset points',
             fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))
"""xy=(x0,y0)是打印起始坐标,xycoords='',表明xy的依据是我们的数据
xytext=（+30，-30）是设置文本位置与xy的相对位置
textcoords=''设置对位置描述
fontsize字体
arrowprops箭头设置"""

plt.text(-3.7,3,r'$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size':16,'color':'r'})

plt.show()