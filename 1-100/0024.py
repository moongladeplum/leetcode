# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
    
        # New head is the second node
        new_head = head.next
        
        back = head
        front = head.next
        
        while back and front:
            temp = front.next
            
            # Swap the pair
            front.next = back
            
            # Check if we have another pair
            if temp and temp.next:
                back.next = temp.next
                back = temp
                front = temp.next
            else:
                back.next = temp
                break
    
        return new_head
