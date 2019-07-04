
#蒙特卡洛法求圆周率
from random import random
from time import perf_counter
darts=1000*1000 #总的投掷次数
hots=0.0 #当前圆内的点数
star t= perf_counter
for i in range (darts+1)
x,y=random(),random()
dist=pow(x**2+y**2,0.5)
if dist <+1.0:
    hits+hits+1
pi=4*(hits/darts)
print("圆周率的值是：{}".format(pi))
print("运行时间是：{：.5f}s".format(perf_counter()-start))