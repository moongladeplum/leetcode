# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None or list2 is None:
            return list1 or list2
        temp = ListNode()
        tail = temp
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1  #point temp merged list to the smaller node
                list1 = list1.next #move the list1 pointer forward
            else:
                tail.next = list2  #point temp merged list to the smaller node
                list2 = list2.next #move the list2 pointer forward
            tail = tail.next       #move temp tracking pointer forward
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return temp.next
