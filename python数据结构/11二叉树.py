
"""二叉树的性质(特性)
性质1: 在二叉树的第i层上至多有2^(i-1)个结点（i>0）
性质2: 深度为k的二叉树至多有2^k - 1个结点（k>0）
性质3: 对于任意一棵二叉树，如果其叶结点数为N0，而度数为2的结点总数为N2，则N0=N2+1;
性质4:具有n个结点的完全二叉树的深度必为 log2(n+1)
性质5:对完全二叉树，若从上至下、从左至右编号，则编号为i 的结点，其左孩子编号必为2i，
其右孩子编号必为2i＋1；其双亲的编号必为i/2（i＝1 时为根,除外）"""
class Node(object):
    """"树的节点"""
    def __init__(self,item):
        self.elem=item
        self.lchild=None
        self.rchild=None

class Tree(object):
    def __init__(self):
        self.root=None


    def add(self,item):#用广度遍历；队列的形式
        node=Node(item)
        if self.root is None:#即使元素是NOne也会进入循环，所以我们在这里加一个条件控制  解决这种情况
            self.root=node
        else:
            queue=[self.root]
            while queue:#只要队列不为空就一直进行循环
                cur_node=queue.pop(0)#取出一个节点分别查看左孩子右孩子是不是存在
                if  cur_node.lchild is None:
                    cur_node.lchild=node#不存在的话就加在这个位置
                    return
                else:
                    queue.append(cur_node.lchild)#存在的话加入到队列尾部；准备查右孩子是不是存在
                if cur_node.rchild is None:
                    cur_node.rchild=node
                    return
                else:
                    queue.append(cur_node.rchild)


    def breadth_travel(self):#广度遍历(层次遍历）

        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node=queue.pop(0)
            print(cur_node.elem,end='')
            if  cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if  cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    """深度遍历：
    先序：根左右；
    中序左根右；
    后序 左右根"""
    def  preorder(self,node):#这里使用的是递归的思路

        if node is None:
            return
        print(node.elem,end='')
        self.preorder(node.lchild)
        self.preorder(node.rchild)



    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem, end='')
        self.inorder(node.rchild)

    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem, end='')


if  __name__=='__main__':
    tree=Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print('')
    tree.preorder(tree.root)
    print('')
    tree.inorder(tree.root)
    print('')
    tree.postorder(tree.root)
    print('')

