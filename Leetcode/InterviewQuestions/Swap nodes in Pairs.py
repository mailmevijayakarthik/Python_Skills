class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SwapNodes:
    def swapPairs(self, head: ListNode) -> ListNode:
        d1=d=ListNode(0)
        d.next=head
        while d.next and d.next.next:
            p=d.next
            q=p.next
            d.next,p.next,q.next=q,q.next,p
            d=p
        return d1.next

swap=SwapNodes()
list=ListNode([1,2,3,4])

newlist=swap.swapPairs(list)
print(newlist.val)