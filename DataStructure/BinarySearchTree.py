class Node(object):
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

class BinarySearchTree(object):
    """
    BinarySearchTree is a Data structure which uses Binary search principle
    Every node has at most 2 childs
    Left child is small than the parent(root)
    Right child is larger than the parent(root)
    """
    def __init__(self):
        self.root=None

    def insert(self,data):
        if not self.root:
            self.root=Node(data)
        else:
            self.insertNode(data,self.root)

    def insertNode(self,data,node):
        if data < node.data:
            if node.leftchild:
                self.insertNode(data,node.leftchild)
            else:
                node.leftchild=Node(data)
        else:
            if node.rightchild:
                self.insertNode(data,node.rightchild)
            else:
                node.rightchild=Node(data)

    def getminimumvalue(self):
        if self.root:
            return self.getMinum(self.root)

    def getMinum(self,node):
        if node.leftchild:
            return self.getMinum(node.leftchild)
        print("Smallest value %s" % node.data)
        return node.data

    def getHighestvalue(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self,node):
        if node.rightchild:
            return self.getMax(node.rightchild)
        print("Hightest value %s" %node.data )
        return node.data

    def traverse(self):
        if self.root:
            return self.traverseInorder(self.root)

    def traverseInorder(self,node):
        if node.leftchild:
             self.traverseInorder(node.leftchild)
        print("%s"%node.data)
        if node.rightchild:
             self.traverseInorder(node.rightchild)

    def remove(self,data):
        if self.root:
            return self.removeitem(data,self.root)

    def removeitem(self,data,node):
        if not node:
            return node
        if data<node.data:
            node.leftchild= self.removeitem(data,node.leftchild)
        elif data>node.data:
            node.rightchild= self.removeitem(data,node.rightchild)
        else :
            # For deleting item with no child(leaf node)
            if not node.leftchild and not node.rightchild:
                print("Deleting a leaf node ")
                del node
                return None
            # For deleting items with one child
            if not node.leftchild:
                print("Deleting the node which has only right child")
                tempnode = node.rightchild
                del node
                return tempnode
            elif not node.rightchild:
                print("Deleting the node which has only left child")
                tempnode = node.leftchild
                del node
                return tempnode
            elif  node.rightchild and node.leftchild:
                print("Deleting the node which has both left and right child")
                tempnode = self.getPredecessor(node.leftchild)
                node.data = tempnode.data
                node.leftchild = self.removeitem(tempnode.data, node.leftchild)

        return node


    def getPredecessor(self,node):
        if node.rightchild:
            return self.getPredecessor(node.rightchild)
        return node


binarySearchTree=BinarySearchTree()
binarySearchTree.insert(10)
binarySearchTree.insert(20)
binarySearchTree.insert(30)
binarySearchTree.insert(15)
binarySearchTree.insert(25)
#binarySearchTree.insert(3)
#binarySearchTree.getminimumvalue()
#binarySearchTree.getHighestvalue()
binarySearchTree.traverse()
binarySearchTree.remove(30)
binarySearchTree.traverse()




