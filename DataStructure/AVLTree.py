class Node(object):
    def __init__(self,data):
        self.data=data
        self.height=0
        self.leftchild=None
        self.rightchild=None

class AVLTree(object):
    """
    Height parameter  h
    h = max(leftchild.height - rightchild.height)+1
    If Difference in h parameter of left and right child is other than -1 <= h <= 1 then the Tree is unbalanced ==> Then we need to do rotation

    """
    def __init__(self):
        self.root=None

    def calcHeight(self,node):
        if not node:
            return -1

        return node.height

    def insert(self,data):
        self.root=self.insertNode(data,self.root)

    def insertNode(self,data,node):
        if not node:
            return Node(data)
        if data<node.data:
            node.leftchild=self.insertNode(data,node.leftchild)
        else :
            node.rightchild=self.insertNode(data,node.rightchild)
        node.height = max(self.calcHeight(node.leftchild), self.calcHeight(node.rightchild)) + 1

        return self.settleViolation(data,node)

    def settleViolation(self,data,node):
        balance=self.calcBalance(node)
        #case 1 : Balance > 1 means heavy left tree situation
        if balance>1 and data <node.leftchild.data:   # insert 5 to the tree which has 10,20,30
            print("LL situation results to Right Rotation..")
            return self.rotateRight(node)
        # Case 2 : RR so single Left rotation
        if balance<-1 and data>node.rightchild.data:  # insert 40 to the tree which has 10,20,30
            print("RR situation results to Left Rotation ..")
            return self.rotateLeft(node)

        if balance>1 and data> node.leftchild.data:  # insert 15 to the tree which has 10,20,30
            print("Left Right heavy situation .. ")
            node.leftchild=self.rotateLeft(node.leftchild)
            return self.rotateRight(node)
        if balance < -1 and data < node.rightchild.data:  #
            print("Left Right heavy situation .. ")
            node.rightchild = self.rotateRight(node.rightchild)
            return self.rotateLeft(node)

        return node


    def traverse(self):
        if self.root:
            self.traverseInorder(self.root)

    def traverseInorder(self,node):
        if node.leftchild:
            self.traverseInorder(node.leftchild)
        print("%s" %node.data)
        if node.rightchild:
            self.traverseInorder(node.rightchild)


    # If the Balance value returns >1 it is left heavy tree --> need right rotation
    # If the Balance value returns <1 it is right heavy tree --> need left rotation

    def calcBalance(self,node):
        if not node:
            return 0
        return self.calcHeight(node.leftchild) - self.calcHeight(node.rightchild)

    def rotateRight(self,node):
        print("Right rotation due to left heavy tree ")
        templeftchild=node.leftchild
        t=templeftchild.rightchild
        templeftchild.rightchild=node
        node.leftchild = t
        node.height= max(self.calcHeight(node.leftchild),self.calcHeight(node.rightchild))+1
        templeftchild.height=max(self.calcHeight(templeftchild.leftchild),self.calcHeight(templeftchild.rightchild))+1

    def rotateLeft(self,node):
        print("Left rotation due to Right heavy tree ")
        tempRightchild=node.rightchild
        t=tempRightchild.leftchild
        tempRightchild.leftchild=node
        node.rightchild = t
        node.height= max(self.calcHeight(node.leftchild),self.calcHeight(node.rightchild))+1
        tempRightchild.height=max(self.calcHeight(tempRightchild.leftchild),self.calcHeight(tempRightchild.rightchild))+1


avltree=AVLTree()
#print(avltree.__doc__)
avltree.insert(10)
avltree.insert(20)
avltree.traverse()
avltree.insert(30)

avltree.traverse()