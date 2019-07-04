class Node(object):
    """节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleCycleLinkList(object):
    def  __init__(self,node=None):
        self.__head=node
        if node:
            node.next=node

    def is_empty(self):
        return self.__head==None

    def length(self):
        if self.is_empty():
            return 0
        else:
            cur=self.__head
            count=1
            while cur.next !=self.__head:
                count+=1
                cur=cur.next
            return count

    def travel(self):
        if self.is_empty():
            return None
        else:
            cur=self.__head
            while cur.next !=self.__head:
                print(cur.elem,end='')
                cur=cur.next
            print(cur.elem)
    def add(self,item):
        #头插法
        node=Node(item)
        if self.is_empty():
            self.__head=node
            node.next=node
        else:
            cur=self.__head
            while cur.next!=self.__head:
                cur=cur.next
            #退出循环时，cur指向尾节点
            node.next=self.__head
            self.__head=node
            cur.next=node

    def append(self, item):
        """链表尾部添加元素, 尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # node.next = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self,pos,item):
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            pre=self.__head
            count=0
            while count<(pos-1):
                count+=1
                pre=pre.next
                #当退出循环pre指向pos-1位置
            node=Node(item)
            node.next=pre.next
            pre.next=node

    def search(self,item):
        if self.is_empty():
            return False
        else:
            cur=self.__head
            while cur.next!=self.__head:
                if cur.elem==item:
                    return True
                else:
                    cur=cur.next
            if cur.elem==item:
                return True
            return False

    def remove(self,item):
        cur=self.__head
        pre=None
        while cur.next!=self.__head:
            if cur.elem==item:
                #看看是否为头结点
                if cur==self.__head:
                    rear=self.__head
                    while rear.next!=self.__head:
                        rear=rear.next
                    self.__head=cur.next
                    rear.next=self.__head
                    self.__head=cur.next
                else:
                    #中间节点
                    pre.next=cur.next
                return
            else:
                pre=cur
                cur=cur.next
        #尾节点
        if cur.elem==item:
            if cur==self.__head:
                self.__head=None
            else:
                pre.next=cur.next


if __name__=='__main__':
    ll = SingleCycleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # 8 1 2 3 4 5 6
    ll.insert(-1, 9)  # 9 8 1 23456

    ll.insert(3, 100)  # 9 8 1 100 2 3456
    ll.remove(100)
    ll.travel()


