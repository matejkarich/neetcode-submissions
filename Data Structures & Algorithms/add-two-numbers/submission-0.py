# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = l1, l2
        runningSum = 0
        runningSum += self.parseList(head1)
        runningSum += self.parseList(head2)
        print(runningSum)
        return self.convertToList(runningSum, l1)

    def parseList(self, head):
        runningSum = 0
        digits = 1
        while head:
            runningSum += (digits * head.val)
            digits = digits * 10
            head = head.next
        return runningSum

    def convertToList(self, val, head):
        prev = curr = head
        while val != 0:
            if curr:
                curr.val = val % 10
                val = val // 10
                prev = curr
                curr = curr.next
            else:
                prev.next = ListNode(val % 10, None)
                prev = prev.next
                val = val // 10
        return head



