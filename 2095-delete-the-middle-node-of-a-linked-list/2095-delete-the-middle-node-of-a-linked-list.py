# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        head1, head2 = head, head
        while head1:
            n += 1
            head1 = head1.next
        if n == 1:
            return None
        i, prev = 0, head
        while i < n//2:
            prev = head2
            head2 = head2.next
            i += 1
            
        while head2.next:
            head2.val = head2.next.val
            prev = head2 
            head2 = head2.next
        prev.next = None
        return head
        