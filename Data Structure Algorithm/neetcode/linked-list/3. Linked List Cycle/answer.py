# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        turtle = head
        rabbit = head

        while rabbit and rabbit.next:
            turtle = turtle.next
            rabbit = rabbit.next.next

            if not turtle or not rabbit:
                return False

            if turtle.val == rabbit.val:
                return True

        return False
        