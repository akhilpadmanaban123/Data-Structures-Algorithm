# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # link lastr node to the head to create a cycle
        # the position of rotation is k% length of list
        

        # if list is empty
        if not head:
            return head
        
        length = 1
        dummy = head

        while dummy.next:
            dummy = dummy.next
            length += 1         # length of the list
        
        position = k % length # position of rotation start
        if position == 0:
            return head  # start of the list again
        
        current = head
        for _ in range(length - position-1):  # upto the next node of the position  
            current = current.next
        
        new_head =current.next
        current.next = None # breaking the list
        dummy.next = head  # linking the last to the first

        return new_head

