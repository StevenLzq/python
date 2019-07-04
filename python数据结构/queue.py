#队列 当一个元素被加入到队列之后，它就从队尾开始向队首前进，
# 直到它成为下一个即将被移出队列的元素。

#现实中排队会比较像
"""队列一个应该知道点事，如果入队操作多就把列表尾部做队列为，
如果出队操作多的话就把列表为做队列头"""
class Queue(object):
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def  enqueue(self,item):#从头部入队
        self.items.insert(0,item)#在这里我们以列表头为队列尾部 方便进行pop

    def dequeue(self):#尾部出队
        return self.items.pop()

    def size(self):
        return len(self.items)

if __name__=='__main__':
    q=Queue()
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size())
    print(q.isEmpty())
    a=q.dequeue()
    print(a)
