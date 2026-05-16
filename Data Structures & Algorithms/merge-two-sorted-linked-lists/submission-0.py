# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1, curr2 = list1, list2

        while curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                while curr1 is not None and curr2 is not None and curr1.val <= curr2.val:
                    prev1 = curr1
                    curr1 = curr1.next
                prev1.next = curr2

            else:
                while curr2 is not None and curr1 is not None and curr2.val <= curr1.val:
                    prev2 = curr2
                    curr2 = curr2.next
                prev2.next = curr1
        
        return list2