class BinaryTree(object):
    def __init__(self,item):
        self.key=item
        self.leftChild=None
        self.rightChild=None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newitem):
        if self.rightChild is None:
            self.rightChild=BinaryTree(newitem)
        else:
            t=BinaryTree(newitem)
            t.rightChild=self.rightChild
            self.rightChild=t

    def getRightChild(self):
            if self.rightChild is None:
                return self.rightChild
            else:
                return self.rightChild.key

    def getLeftChild(self):
        if self.leftChild is None:
            return self.leftChild#如果leftChild不为空  那么他就是一个树，
            # 树在print里面无法直接显示，所以下一步应该打印的是他的key属性
        else:
            return self.leftChild.key

    def setRootVal(self,newVal):
        self.key=newVal

    def getRootVal(self):
        return self.key
if __name__=="__main__":

    r=BinaryTree(1)
    print(r.getRootVal())
    print(r.getLeftChild())
    r.insertLeft(2)
    print(r.getLeftChild())
    r.insertRight('c')
    print(r.getRightChild())
    r.setRootVal('hello')
    print(r.getRootVal())
