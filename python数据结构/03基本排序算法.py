

########################选择排序###############################################
'''
我们首先来分析一下选择排序的思路，我们是首先拿出第一个数依次和后面所有元素比较
如果有一个元素比他小，我们就把新的最小的下标保存，到最后把最小的下标和0坐标交换；
按照这样一个思路，一次对每个元素进行操作。

'''
def swap(list,i,j):
    temp=list[i]
    list[i]=list[j]
    list[j]=temp

a=[7,3,1,5,4]

'''
def selectionSort(list):
    i=0
    while i<len(list)-1:
        mindex=i
        j=i+1
        while j<len(list):
            if list[j]<list[mindex]:
                mindex=j
            j +=1
        if mindex !=i:
            swap(list,mindex,i)

        i+=1

    return list

a=[7,3,1,5,4]
print(selectionSort(a))

#

'''
#######################################################################
#冒泡排序
'''
从列表开头开始比较一对数据大小，每当成对顺序不对的时候就交换二者位置
'''
'''
def bubleSort(list):
    n=len(list)
    while n>1:
        i=1
        while i<n:
            if list[i]<list[i-1]:
                swap(list,i,i-1)
            i +=1
        n-=1
    return list
print(bubleSort(a))

'''


'''

##我们可以在这个基础上对，最好的情况进新一点小修改
def buble(list):
    n=len(list)
    while n>1:
        i=1
        swapped=False
        while i<n:
            if list[i]<list[i-1]:
                swap(list,i,i-1)
                swapped=True
            i+=1
        if not swapped:return list
        n-=1
    return list

print(buble(a))
'''
##########################################################################

#插入排序


