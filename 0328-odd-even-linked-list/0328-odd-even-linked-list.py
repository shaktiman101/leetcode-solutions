# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd, even = head, head.next
        even_orig = even
        
        while even and even.next:
            ptr = even.next
            odd.next = ptr
            odd = odd.next
            even.next = ptr.next
            even = even.next
        odd.next = even_orig
        return head
        