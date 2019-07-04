'''



####################################绘制简单折线图#############################
import matplotlib.pyplot as plt


input_data=[1,2,3,4,5]
squares=[1,4,9,16,25]
plt.plot(input_data,squares,linewidth=5)#设置线宽

plt.title('squares number',fontsize=24)#设置标题，和标题字号

plt.xlabel('value',fontsize=14)#设置标签
plt.ylabel('squares of value',fontsize=14)

plt.tick_params(axis='both',labelsize=14)#设置刻度标记大小

plt.show()

#########################scatter绘制散点图#########################################
import matplotlib.pyplot as plt
x_value=[1,2,3,4,5]
y_value=[1,4,9,16,25]
plt.scatter(x_value,y_value,s=100)
plt.title('square number',fontsize=24)
plt.xlabel('value',fontsize=14)
plt.ylabel('square of value',fontsize=14)

plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()

'''
##########################################################################
import matplotlib.pyplot as plt

x_value=list(range(1,1001))

y_value=[x**2 for x in x_value]

plt.scatter(x_value,y_value,c=(0,0,0.8),edgecolor='none',s=40)
#edgecolor='none'删除数据点轮廓,三通道颜色c=(0,0,0.8)越接近0越深

plt.title('square number',fontsize=24)
plt.xlabel('value',fontsize=14)
plt.ylabel('square of value',fontsize=14)
plt.axis([0,1100,0,1100000])#设置坐标轴取值范围
plt.show()