'''在衡量一个算法的时候我们主要考虑准确性、可读性、易维护性、运行时间和内存
这里我们主要从时间方面来做一点测试，会用到一个timeit
'''
'''
'''
from timeit import Timer

#以列表的几个操作来做例子
'''在生成一个列表的时候我们常用的方法
append
+= /+
extend
list(range())
i for i in range列表生成器
'''
def test1():
    li=[]
    for i in range(10000):
        li.append(i)

def test2():
    li=[]
    for i in range(10000):
        li=li+[i]

def test3():
    li=[]
    for i in range(10000):
        li +=[i]


def test4():
    li=[]
    for i in range(10000):
        li.extend([i])

def test5():
    li=[i for i in range(10000)]


def test6():
    li=list(range(10000))


time1=Timer('test1()','from __main__ import test1')
print('append:',time1.timeit(1000))

time2=Timer('test2()','from __main__ import test2')
print('+:',time2.timeit(1000))

time3=Timer('test3()','from __main__ import test3')
print('+=:',time3.timeit(1000))

time4=Timer('test4()','from __main__ import test4')
print('extend:',time4.timeit(1000))

time5=Timer('test5()','from __main__ import test5')
print('i fir i in range:',time5.timeit(1000))

time6=Timer('test6()','from __main__ import test6')
print('list:',time6.timeit(1000))

'''从test2 和test3 对比来看为什么差距那么大呢？
li=li+[i] 这里把li和[i]相加放到一个新的list里面
li+=[i]是把[i]直接加到了li里面
所以+花了大量时间
+=是对+的一种优化
'''

'''
三数之和 a+b+c=1000，a^2+b^2=c^2,求a,b,c
'''
for a in range(1000):
    for b in range(1000):
        for c in range(1000):
            if a+b+c==1000 and a**2+b**2==c**2:
                print('a,b,c',a,b,c)







