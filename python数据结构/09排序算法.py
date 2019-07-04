import  numpy as np



def swap(list,i,j):
    tmp=list[i]
    list[i]=list[j]
    list[j]=tmp

"""冒泡排序（英语：Bubble Sort）是一种简单的排序算法。它重复地遍历要排序的数列，一次比较两个元素，
如果他们的顺序错误就把他们交换过来。遍历数列的工作是重复地进行直到没有再需要交换，
也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

冒泡排序算法的运作如下：

比较相邻的元素。如果第一个比第二个大（升序），就交换他们两个。
对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
针对所有的元素重复以上的步骤，除了最后一个。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。"""

def bubbleSort(list):
    n=len(list)
    while  n>1:#首先这一步就是有n个元素n-1个已经到正确位置那么剩下的一个
        # 就没必要考虑肯定是他的位子因此我们不用重复考虑的是0所以i从1开始
        i=1#只要1到n-1对了0自然不用考虑；当然这里说的是下标
        while i<n:#由于下标比len小一，list[n-1]就是最后一个 第二点因为是内循环所以n是在更新的
            if list[i]<list[i-1]:#前面一个如果比我大就换位置
                swap(list,i,i-1)
            i+=1
        n-=1
    return list

def bubbleSort2(list):
    n=len(list)-1
    count=0
    for i in range(n,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                swap(list,j,j+1)
                count+=1
        if count==0:
            return list
    return list


"""选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。
首先在未排序序列中找到最小（大）元素，存放到排序
序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，
然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
"""
def selectionSort(list):
    n=len(list)-1
    i=0
    while i<n:
        mindex=i
        j=i+1
        while j <n+1:
            if  list[j]<list[mindex]:
                mindex=j
            j+=1
        swap(list,mindex,i)
        i+=1
    return list
def selectionSort2(list):
    n=len(list)
    for i in range(n-1):#先说外循环要做多少次；前n-1个关系确定了那么整个顺序就确定了
        mindex=i

        for j in range(i+1,n):#因为mindex=i；j每次从第i+1个开始
            if list[j]<list[mindex]:
                mindex=j
        if mindex!=i:
            swap(list,i,mindex)

    return list



"""插入排序（英语：Insertion Sort）是一种简单直观的排序算法。
它的工作原理是通过构建有序序列，对于未排序数据，
在已排序序列中从后向前扫描，找到相应位置并插入。插入排序在实现上，
在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。"""

def  insertSort(list):
    n=len(list)
    for i in range(1,n):#第一个元素自成有序序列  所以从1开始到n-1
        for j in range(i,0,-1):#每次添加一个过来到新的有序序列，新添加的依次在有序序列中找自己位置
            if list[j]<list[j-1]:
                swap(list,j,j-1)
            else:
                break#break和continue；break直接退出循环，continue不执行本循环下面的代码回到循环开始
    return list

"""希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本
希尔排序是非稳定排序算法。该方法因DL．Shell于1959年提出而得名。 希尔排序是把记录按下标的一定增量分组，
对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，
当增量减至1时，整个文件恰被分成一组，算法便终止。"""

def shellSort(list):

    n=len(list)
    gap=n//2
    while gap>0:
        for i in range (gap,n):
            j=i
            while j>0:
                if list[j]<list[j-gap]:
                    swap(list,j,j-gap)
                else:break
        gap //=2
    return list


if  __name__=='__main__':
    a=[2,4,1,5,3,7,6]
    b=[9,8,7,6,5,4,3,2,1]
    print(a)
    print('bubleSort',bubbleSort(a))
    print('bubleSort2',bubbleSort2(a))
    print('selectionSort',selectionSort(a))
    print('selectionSort2', selectionSort2(b))
    print('insertSort',insertSort(a))
    print('shellSort',shellSort(b))


