from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current_pointer = result
        carry = 0

        while (l1 or l2) or carry != 0:
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0
            val_sum = v1 + v2 + carry
            carry = 0
            
            if val_sum >= 10: 
                carry = val_sum // 10
                val_sum = val_sum % 10

            current_pointer.next = ListNode(val_sum)
            current_pointer = current_pointer.next

            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next

        return result.next