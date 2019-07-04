"""
用python类来实现数组的一些基本操作
"""

class Arrayl(object):
    def __init__(self,capacity,fillValue=None):
        self._items=list()
        for count in range(capacity):
            self._items.append(fillValue)
            
    def __len__(self):
        return len(self._items)
    
    def __str__(self):
        return str(self._items)
    
    def  __iter__(self):
        return iter(self._items)
    
    def __getitem__(self,index):
        return self._items[index]
    
    def __setitem__(self,index,newItem):
        self._items[index]=newItem


if  __name__=='__main__':

    a=Arrayl(5)
    print(a)
    print(len(a))
    for i in range(len(a)):
        a[i]=i+1

    for item in a:
        print(item)


    """数组可以看成是列表一个受限制的版本"""
    """逻辑大小和物理大小 逻辑大小就是装了几个 物理大小就是能装几个
    """
    #数组操作-增加数组大小
    DEFAULT_CAPACITY=5
    logicalSize=0
    a=Arrayl(DEFAULT_CAPACITY)

    if logicalSize==len(a):
        tmp=Arrayl(len(a)+1)     #create a  array
        for i in range(logicalSize):
            tmp[i]=a[i]   #copy data   from  the old
        a=tmp    #reset the old array variable  to the new array


    #减小数组大小

    if logicalSize<=len(a)//4 and len(a)>DEFAULT_CAPACITY*2:
        tmp=Arrayl(len(a)//2)
        for  i in range (logicalSize):
            tmp[i]=a[i]
        a=tmp


    #在数组中插入一项
    """插入一项就是后面所有的item往后移动一个格子"""
    logicalSize +=1
    targetindex=3
    newitem=4
    for i in range (logicalSize,targetindex,-1):#这句不理解可以多试试就明白了   本身前前面大后面小是无法read的
        a[i]=a[i-1]
    a[targetindex]=newitem



    #从数组中删除一项

    for  i in range(targetindex,logicalSize-1):
        a[i]=a[i+1]
    logicalSize-=1



"""链表"""




