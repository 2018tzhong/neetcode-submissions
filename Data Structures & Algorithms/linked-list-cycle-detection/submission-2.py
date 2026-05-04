# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = head.next if head else None
        p2 = head.next.next if head and head.next else None
        while p1:
            if p2 != None and p1 == p2:
                print(p2.val, p1.val)
                return True
            p1 = p1.next
            p2 = p2.next.next if p2 and p2.next and p2.next.next else None
        return False