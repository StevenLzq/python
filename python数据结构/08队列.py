class Queue(object):
    def __init__(self):
        self.__list=[]

    def  enqueue(self,item):
        #在这里我们假设入队情况多一点，我们从列表的尾部入队复杂度为O（1）
        self.__list.append(item)

    def dequeue(self):
        #从头头部加入列表复杂度为O(n)
        return self.__list.pop(0)

    def is_empty(self):
        return self.__list==None

    def  size(self):
        return len(self.__list)


if __name__=='__main__':
    q=Queue()
    print(q.is_empty())
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())



