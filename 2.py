# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #initialize values
        dummy = ListNode()
        result = dummy
        total = carry = 0
        #traverse list
        while l1 or l2 or carry:
            #calc sum and iterate
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            #checking carry and zero using modulo and division
            num = total % 10
            carry = total // 10
            #create new node with the digit and add it to linked list
            dummy.next = ListNode(num)
            dummy = dummy.next
        return result.next
