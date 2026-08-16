# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        currNode = head
        prevGroup = None
        nextGroup = None
        while(result := self.hasRemainingGroup(currNode, k))[0]:
            headOfGroup = result[1]
            currNode = result[2]
            nextGroup = self.reverseGroup(headOfGroup, currNode)
            if not prevGroup:
                prevGroup = headOfGroup
                head = currNode
            else:
                prevGroup.next = currNode
                prevGroup = headOfGroup
            currNode = nextGroup
        if prevGroup:
            prevGroup.next = currNode
        return head

    def hasRemainingGroup(self, currNode, k):
        if not currNode:
            return (False, None, None)
        headOfGroup = currNode
        while k > 1:
            currNode = currNode.next
            if not currNode:
                return (False, headOfGroup, currNode)
            k -= 1
        return (True, headOfGroup, currNode)

    def reverseGroup(self, headOfGroup, currNode):
        start = headOfGroup
        curr = headOfGroup.next
        if not curr:
            return
        nex = curr.next
        start.next = None
        curr.next = start
        temp = None
        while curr != currNode:
            if not nex:
                return None
            temp = nex.next
            nex.next = curr
            curr = nex
            nex = temp
        return temp
        
        