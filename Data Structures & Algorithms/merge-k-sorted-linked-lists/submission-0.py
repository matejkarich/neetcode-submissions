# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        merged = lists[0]
        curr = 1
        while curr < len(lists):
            merged = self.mergeTwoLists(merged, lists[curr])
            curr += 1
        return merged

    def mergeTwoLists(self, list1, list2):
        dummy = node = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
                node = node.next
            else:
                node.next = list2
                list2 = list2.next
                node = node.next
        if list1:
            node.next = list1
        if list2:
            node.next = list2
        return dummy.next