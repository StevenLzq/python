""""线性数据结构"""
#栈stack
#队列queue
#双端队列 deque
#列表 list

"""线性结构有两个端，有时候，我们称这两端为“左”和“右”，或者“前”和
“后”，或者“顶”和“底”。其实名字不重要，区别线性结构和其他结构的依据是项进行添加和
删除的方式，尤其是添加和删除发生的位置"""


#栈遵循的是后进先出的原则，在形式上像一堆碟子，刚洗的放在最上面，最先被拿走使用
#栈的两个最基本操作是 push压入 pop弹出

class Stack(object):
    def  __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            self.stack.pop()
        else:
            raise LookupError('stack is empty')#
    def isEmpty(self):
        return bool(self.stack)

    def  top(self):#取出栈顶元素
        return self.stack[-1]

    def size(self):
        return len(self.stack)
if __name__=='__main__':
    s=Stack()
    s.push('a')
    s.push(23)
    print(s.size())
    s.pop()
    print(s.size())

