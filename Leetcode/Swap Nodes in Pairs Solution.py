# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def swapPairs(self, head):
        newNode = ListNode(head)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = None

solu=Solution(object)
solu.swapPairs(1)

