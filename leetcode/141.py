# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        store=set()
        curr=head
        while(curr!=None):
            if(curr in store):
                return True
            store.add(curr)
            curr=curr.next
        return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow,fast=head,head
        while(fast!=None and fast.next!=None):
            if(slow==fast):
                return True
            slow=slow.next
            fast=fast.next.next
        return False

