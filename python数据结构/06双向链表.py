class Node(object):
    def __init__(self,item):
        self.elem=item
        self.next=None
        self.prev=None
class DoubleLinkList(object):
    def __init__(self,node=None):
        self.__head=node

    def is_empty(self):
        return self.__head is None

    def length(self):
        cur=self.__head
        count=0
        while cur!=None:
            count+=1
            cur=cur.next
        return count

    def travel(self):
        cur=self.__head
        while cur!=None:
            print(cur.elem,end=' ')
            cur=cur.next
        print('')

    def add(self,item):
        node = Node(item)
        if self.is_empty():
            self.__head=node

        node.next=self.__head
        node.next.prev=node
        self.__head=node
    def append(self, item):
        """链表尾部添加元素, 尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self,pos,item):
        node=Node(item)
        if pos<0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            cur=self.__head
            count=0
            while count<pos:
                count+=1
                cur=cur.next

            node.next=cur
            node.prev=cur.prev
            cur.prev.next=node
            cur.prev=node

    def search(self,item):
        cur=self.__head
        while cur!=None:
            if cur.elem==item:
                return True
            else:
                cur=cur.next
        return False


    def remove(self,item):
        cur=self.__head
        while cur!=None:
            if cur.elem==item:
                if  cur==self.__head:
                    self.head=cur.next
                    if cur.next:
                        #判断链表是否只有一个节点
                        cur.next.prev=None
                else:
                    cur.prev.next=cur.next
                    if cur.next:
                         cur.next.prev=cur.prev
                break
            else:
                cur=cur.next





if __name__ == "__main__":
    ll = DoubleLinkList()
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
    ll.travel()
    ll.insert(-1, 9)  # 9 8 1 23456
    ll.travel()
    ll.insert(3, 100)  # 9 8 1 100 2 3456
    ll.travel()
    ll.insert(10, 200)  # 9 8 1 100 23456 200
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()
