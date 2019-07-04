import matplotlib.pyplot as plt

from random_walk import RandomWalk
while True:
    rw=RandomWalk()
    rw.fill_walk()
    plt.figure(figsize=(10,6))#设置窗口尺寸大小

    point_numbers=list(range(rw.num))

    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=15)

    plt.scatter(0,0,c='green',edgecolor='none',s=100)#重新绘制起点
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',s=100)#重新绘制终点

    plt.axes().get_xaxis().set_visible(False)#隐藏坐标轴
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running=input('make another walk?(y/n)')
    if keep_running=='n':
        break