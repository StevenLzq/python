#以列表嵌套的方式来理解二叉树


def  binaryTree(r):
    return [r,[],[]]
def  insertLeft(root,newBranch):
    t=root.pop(1)
    if len(t)>1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root
def insertRight(root,item):
    t=root.pop(2)
    if len(t)>1:
        root.insert(2,[item,[],t])
    else:
        root.insert(2,[item,[],[]])
    return root
def getRootVal(root):
    return root[0]
def setRootVal(root,newVal):
    root[0]=newVal
def getLeftChild(root):
    return root[1]
def getRightChild(root):
    return root[2]

mytree=binaryTree('a')
insertLeft(mytree,'b')
print(mytree[1])
insertRight(mytree,'c')
insertRight(getRightChild(mytree),'d')
insertLeft(getRightChild(mytree),'e')
print(mytree)