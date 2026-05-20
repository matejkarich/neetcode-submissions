# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = self.reverseList(head)
        if not head.next and n == 1:
            return None
        prev = curr = head
        while curr and n > 1:
            prev = curr
            curr = curr.next
            n = n - 1
        prev.next = curr.next

        return self.reverseList(head)

    def reverseList(self, head):
        if not head or not head.next:
            return head

        curr = head
        nex = head.next

        while nex:
            temp = nex.next
            nex.next = curr
            curr = nex
            nex = temp
        head.next = None

        return curr
        
        