# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = ListNode()
        prev.next = head
        curr = prev

        while head:
            if head.val == val:
                curr.next = head.next
            else:
                curr = curr.next

            head = head.next

        return prev.next