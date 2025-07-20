# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # node_count = 0
        # curr = head

        # while curr:
        #     curr = curr.next
        #     node_count += 1

        # target_node = node_count-n+1
        # curr = head
        # prev = None

        # while target_node != 1:
        #     prev = curr
        #     curr = curr.next
        #     target_node -= 1
        
        # if prev is None:
        #     return head.next
        # prev.next = curr.next
        # return head

        # dummy = ListNode(0, head)
        # left = dummy
        # right = head

        # while n > 0:
        #     right = right.next
        #     n -= 1
        
        # while right:
        #     right = right.next
        #     left = left.next

        # left.next = left.next.next
        # return dummy.next

        left, right = head, head
        for _ in range(n):
            right = right.next

        if not right:
            return head.next

        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return head


