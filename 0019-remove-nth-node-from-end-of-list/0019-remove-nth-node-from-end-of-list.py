# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = 0
        cur = head
        while cur:
            nodes += 1
            cur = cur.next
        # if nodes == 1:
        #     return head.next

        node_from_beginning = nodes-n

        cur = head
        prev = cur
        cur = cur.next
        count = 1
        if not cur or node_from_beginning==0:
            return cur

        while cur:
            if count == node_from_beginning:
                prev.next = cur.next
            prev = cur
            cur = cur.next
            count += 1

        return head