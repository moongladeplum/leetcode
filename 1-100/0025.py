# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge case: if k is 1 or list is empty, no reversal needed
        if k == 1 or not head:
            return head
        # Create dummy node to handle edge cases easily
        dummy = ListNode(0)
        dummy.next = head
        # 'prev' points to the node before the current group
        prev = dummy
        while True:
            # Check if there are at least k nodes remaining
            # 'check' will traverse to find the kth node
            check = prev
            for i in range(k):
                check = check.next
                if not check:  # Less than k nodes left
                    return dummy.next
            # We have k nodes to reverse
            # 'curr' points to the first node of the group
            curr = prev.next
            # Reverse k nodes
            # Standard linked list reversal for k nodes
            for i in range(k - 1):
                # Move the node after 'curr' to the front of the group
                temp = curr.next
                curr.next = temp.next
                temp.next = prev.next
                prev.next = temp
            # Move 'prev' to the end of the reversed group
            # 'curr' is now the last node of the reversed group
            prev = curr
        return dummy.next
