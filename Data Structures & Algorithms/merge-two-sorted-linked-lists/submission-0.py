# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        curr_head = ListNode()
        curr_node = curr_head
        while p1 and p2:
            if p1.val < p2.val:
                curr_node.next = p1
                p1 = p1.next
                curr_node = curr_node.next
            else:
                curr_node.next = p2
                p2 = p2.next
                curr_node = curr_node.next
        if p1:
            curr_node.next = p1
        elif p2:
            curr_node.next = p2
        return curr_head.next