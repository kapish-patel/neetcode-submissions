# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = head
        current = head
        back = None
        
        while current:
            front = front.next
            current.next = back
            back = current
            current = front
        
        return back

        
        