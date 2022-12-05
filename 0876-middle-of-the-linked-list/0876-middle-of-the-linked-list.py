# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        p, dp = head, head
        while dp and dp.next:
            
            p = p.next
            dp = dp.next.next 
        return p