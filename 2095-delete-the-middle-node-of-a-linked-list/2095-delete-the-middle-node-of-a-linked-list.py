# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node = head
        temp = head
        if not head.next:
            head = None
        else:

            while temp.next or temp is None:
                prev = node
                node = node.next
                if temp.next.next:
                    temp = temp.next.next
                else:
                    temp = temp.next
            prev.next = prev.next.next

        return head