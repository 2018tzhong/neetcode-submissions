# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        curr_node = head
        if not head.next:
            return head
        next_node = head.next
        next_next_node = next_node.next
        head.next = None
        while next_node:
            next_node.next = curr_node
            curr_node = next_node
            next_node = next_next_node
            next_next_node = next_next_node.next if next_next_node else None

        return curr_node