# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head.next:
            return None
        temp = head
        node = head
        prev = None

        while temp and temp.next:
            temp = temp.next.next
            prev = node
            node = node.next
        prev.next = prev.next.next

        return head