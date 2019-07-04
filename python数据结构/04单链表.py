# coding:utf-8
class Node(object):
    """节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """单链表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def append(self,item):
        #尾插法
        node = Node(item)
        if self.is_empty():
            self.__head=node
        else:
            cur=self.__head
            while cur.next!=None:
                cur=cur.next
            cur.next=node

    def add(self,item):
        #头插法
        node=Node(item)
        node.next=self.__head
        self.__head=node



    def insert(self,pos,item):
        node=Node(item)
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
            #关键是找到插入位置的前一个节点pre
        else:
            pre=self.__head
            count=0
            while count<pos-1:
                count+=1
                pre=pre.next
                #当循环结束pre指向pos-1位置
            node.next=pre.next
            pre.next=node


    def remove(self,item):
        #删除具体数据
        #空列表的话 循环不执行满足
        #但是要考虑要删除的在head
        pre=None
        cur=self.__head
        while cur!=None:
            if cur.elem==item:
                #先判断节点是不是head如果是的话
                #是头结点而且链表只有一节点

                if cur==self.__head:
                    self.__head = cur.next
                else:
                    pre.next=cur.next
                break

            else:
                pre=cur
                cur=cur.next

    def search(self,item):
        #查找，给一个数据查看他在不在链表中
        #从头开始遍历
        cur=self.__head
        while cur !=None:
            if cur.elem==item:
                return True
            else:
                cur=cur.next
        return False



'''
if __name__ == '__main__'的意思是：当.py文件被直接运行时，
if __name__ == '__main__'之下的代码块将被运行；当.py文件以
模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
'''
if __name__ == "__main__":
    ll = SingleLinkList()
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
    ll.insert(-1,9)

    ll.insert(3,22)
    ll.remove(6)
    ll.travel()
