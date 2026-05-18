# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        curr1, curr2 = list1, list2
        head = list3 = ListNode()

        while curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                list3.next = curr1
                curr1 = curr1.next
            else:
                list3.next = curr2
                curr2 = curr2.next
            list3 = list3.next

        if curr1 is None:
            list3.next = curr2
        if curr2 is None:
            list3.next = curr1
        
        return head.next