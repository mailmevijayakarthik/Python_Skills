class Node(object):
    def __init__(self,data):
        self.data=data
        self.nextNode=None

class LinkedList(object):
    def __init__(self):
        self.head=None
        self.size=0


    # O(1) time complexity very fast
    def insertatStart(self,data):
        self.size=self.size+1
        newNode =Node(data)
        if not self.head:
            self.head=newNode
        else:
            newNode.nextNode=self.head
            self.head = newNode


    # O(N) complexity for inserting in the end
    def insertatEnd(self,data):
        self.size=self.size+1
        newNode=Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode=actualNode.nextNode

        actualNode.nextNode=newNode

    # O(N) complexity
    def traversethelist(self):
        actualNode = self.head
        while actualNode is not None:
            print("%d" %actualNode.data)
            actualNode=actualNode.nextNode


    def removeitem(self,data):

        if self.head is None:
            return
        self.size=self.size-1
        currentNode=self.head
        previousNode=None

        while currentNode.data!=data:
            previousNode=currentNode
            currentNode=currentNode.nextNode



        if previousNode is None:
            self.head=currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode




mylinklist=LinkedList()
mylinklist.insertatStart(5)
mylinklist.insertatStart(15)
mylinklist.insertatStart(25)
mylinklist.insertatEnd(30)
mylinklist.traversethelist()
mylinklist.removeitem(5)

