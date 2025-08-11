# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        slow = fast = dummy

        for _ in range(n+1):
            fast = fast.next
        # 1-->2-->3-->4-->5   ( n = 2)
        #         f

        while slow and fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next

        # 1 - 2 - 3 - 4 - 5 - 6- 7- 8- 9   

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        cur = head
        while cur:
            l+=1
            cur = cur.next
        targetedNode = l - n  # node to be deleted

        if targetedNode == 0:
            return head.next   # one node

        prev = None
        cur = head
        index = 0
        while index < targetedNode:
            index+=1
            prev = cur
            cur = cur.next
        
        #  1-->2-->3-->4-->5
        #          P   C
        if prev and cur:
            prev.next = cur.next
        return head