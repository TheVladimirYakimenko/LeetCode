# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        overflow = 0
        result_node = ListNode()
        result = result_node

        while l1 is not None or l2 is not None or overflow:
            sum_nodes = (l1.val if l1 else 0) + (l2.val if l2 else 0)
            
            result_node.val = (overflow + sum_nodes) % 10
            overflow = (overflow + sum_nodes) // 10

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next

            if l1 is not None or l2 is not None or overflow:
                result_node.next = ListNode()
                result_node = result_node.next
        
        return result