# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        linked_list = []
        node = head

        while node:
            linked_list.append(node)
            node = node.next

        length = len(linked_list)
        
        for idx in range(length // 2 + (1 * (length % 2))):
            node_left = linked_list[idx]
            node_right = linked_list[length - idx - 1]
            node_left.next = node_right
            node_right.next = linked_list[idx + 1]
        else:
            if length % 2 == 0:
                node_right.next = None
            else:
                node_left.next = None
        